from fastapi import APIRouter, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.order import Order, ShipmentType
from app.models.news import News
import uuid
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    news = db.query(News).order_by(News.created_at.desc()).limit(3).all()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "news": news,
            "now": datetime.now()
        }
    )

@router.post("/calculate")
async def calculate_shipping(
    from_city: str = Form(...),
    to_city: str = Form(...),
    weight: float = Form(...),
    volume: float = Form(...),
    shipment_type: ShipmentType = Form(...)
):
    # Базовые ставки за километр для разных типов перевозок
    base_rates = {
        ShipmentType.AUTO: 100,  # руб/км
        ShipmentType.RAIL: 80,   # руб/км
        ShipmentType.SEA: 60     # руб/км
    }
    
    # Здесь должна быть логика расчета расстояния между городами
    # Пока используем фиксированное расстояние для демонстрации
    distance = 1000  # км
    
    # Расчет стоимости
    base_price = base_rates[shipment_type] * distance
    volume_factor = volume * 1.5  # Учитываем объем
    weight_factor = weight * 2    # Учитываем вес
    
    total_price = base_price + (volume_factor + weight_factor) * 100
    
    return {
        "price": total_price,
        "distance": distance,
        "details": {
            "base_price": base_price,
            "volume_charge": volume_factor * 100,
            "weight_charge": weight_factor * 100
        }
    }

@router.post("/track")
async def track_shipment(tracking_number: str = Form(...), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.tracking_number == tracking_number).first()
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    return {
        "status": order.status,
        "from": order.from_city,
        "to": order.to_city,
        "created_at": order.created_at,
        "tracking_number": order.tracking_number,
        "details": {
            "weight": order.weight,
            "volume": order.volume,
            "shipment_type": order.shipment_type.value
        }
    }

@router.post("/order")
async def create_order(
    from_city: str = Form(...),
    to_city: str = Form(...),
    weight: float = Form(...),
    volume: float = Form(...),
    shipment_type: ShipmentType = Form(...),
    db: Session = Depends(get_db)
):
    # Генерируем уникальный номер отслеживания
    tracking_number = str(uuid.uuid4())
    
    # Создаем новый заказ
    order = Order(
        tracking_number=tracking_number,
        from_city=from_city,
        to_city=to_city,
        weight=weight,
        volume=volume,
        shipment_type=shipment_type,
        status="принят в обработку"
    )
    
    try:
        db.add(order)
        db.commit()
        db.refresh(order)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Ошибка при создании заказа"
        )
    
    return {
        "success": True,
        "tracking_number": tracking_number,
        "message": "Заказ успешно создан"
    }
