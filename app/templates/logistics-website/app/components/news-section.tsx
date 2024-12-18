'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'

const newsItems = [
  { id: 1, type: 'tariff', title: 'Обновление тарифов на автоперевозки', content: 'С 1 июля вступают в силу новые тарифы на автомобильные перевозки.' },
  { id: 2, type: 'rail', title: 'Изменения в железнодорожных перевозках', content: 'РЖД вводит новые правила оформления грузов для железнодорожных перевозок.' },
  { id: 3, type: 'general', title: 'Открытие нового логистического центра', content: 'Мы рады сообщить об открытии нового логистического центра в Екатеринбурге.' },
]

export default function NewsSection() {
  const [filter, setFilter] = useState('all')

  const filteredNews = newsItems.filter(item => filter === 'all' || item.type === filter)

  return (
    <div>
      <div className="mb-4 space-x-2">
        <Button variant={filter === 'all' ? 'default' : 'outline'} onClick={() => setFilter('all')}>Все</Button>
        <Button variant={filter === 'tariff' ? 'default' : 'outline'} onClick={() => setFilter('tariff')}>Тарифы</Button>
        <Button variant={filter === 'rail' ? 'default' : 'outline'} onClick={() => setFilter('rail')}>ЖД перевозки</Button>
        <Button variant={filter === 'general' ? 'default' : 'outline'} onClick={() => setFilter('general')}>Общие</Button>
      </div>
      <div className="space-y-4">
        {filteredNews.map(item => (
          <div key={item.id} className="border p-4 rounded">
            <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
            <p>{item.content}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

