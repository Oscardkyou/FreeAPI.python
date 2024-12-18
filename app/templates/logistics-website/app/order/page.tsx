'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { Textarea } from '@/components/ui/textarea'
import Image from 'next/image'

export default function OrderPage() {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    cargoType: '',
    weight: '',
    volume: '',
    transportType: 'auto'
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically send the form data to your backend
    console.log('Form submitted:', formData)
    alert('Заказ успешно оформлен!')
  }

  return (
    <div className="container mx-auto px-6 py-8">
      <h1 className="text-4xl font-bold mb-8 text-blue-900">Оформление заказа</h1>
      <div className="grid md:grid-cols-2 gap-8">
        <div>
          <Image src="/placeholder.svg?height=400&width=600" alt="Оформление заказа" width={600} height={400} className="rounded-lg shadow-lg" />
        </div>
        <form onSubmit={handleSubmit} className="space-y-6 bg-blue-100 p-6 rounded-lg shadow-lg">
          <div>
            <Label htmlFor="name" className="text-blue-900">ФИО</Label>
            <Input id="name" name="name" value={formData.name} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
          </div>
          <div>
            <Label htmlFor="phone" className="text-blue-900">Телефон</Label>
            <Input id="phone" name="phone" type="tel" value={formData.phone} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
          </div>
          <div>
            <Label htmlFor="cargoType" className="text-blue-900">Тип груза</Label>
            <Input id="cargoType" name="cargoType" value={formData.cargoType} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
          </div>
          <div>
            <Label htmlFor="weight" className="text-blue-900">Вес (кг)</Label>
            <Input id="weight" name="weight" type="number" value={formData.weight} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
          </div>
          <div>
            <Label htmlFor="volume" className="text-blue-900">Объем (м³)</Label>
            <Input id="volume" name="volume" type="number" value={formData.volume} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
          </div>
          <div>
            <Label className="text-blue-900">Предпочтительный вид транспорта</Label>
            <RadioGroup value={formData.transportType} onValueChange={(value) => setFormData({...formData, transportType: value})}>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="auto" id="auto" />
                <Label htmlFor="auto" className="text-blue-900">Автомобильная перевозка</Label>
              </div>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="rail" id="rail" />
                <Label htmlFor="rail" className="text-blue-900">Железнодорожная перевозка</Label>
              </div>
            </RadioGroup>
          </div>
          <Button type="submit" className="bg-yellow-500 text-blue-900 hover:bg-yellow-600">Оформить заказ</Button>
        </form>
      </div>
    </div>
  )
}

