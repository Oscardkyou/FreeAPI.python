'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'

export default function CostCalculator() {
  const [from, setFrom] = useState('')
  const [to, setTo] = useState('')
  const [transportType, setTransportType] = useState('auto')
  const [result, setResult] = useState<{ price: number; duration: number } | null>(null)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically make an API call to calculate the price and duration
    // For this example, we'll just set some dummy values
    setResult({
      price: Math.floor(Math.random() * 10000) + 5000,
      duration: Math.floor(Math.random() * 5) + 1
    })
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6 max-w-md mx-auto">
      <div>
        <Label htmlFor="from">Откуда</Label>
        <Input id="from" value={from} onChange={(e) => setFrom(e.target.value)} required />
      </div>
      <div>
        <Label htmlFor="to">Куда</Label>
        <Input id="to" value={to} onChange={(e) => setTo(e.target.value)} required />
      </div>
      <RadioGroup value={transportType} onValueChange={setTransportType}>
        <div className="flex items-center space-x-2">
          <RadioGroupItem value="auto" id="auto" />
          <Label htmlFor="auto">Автомобильная перевозка</Label>
        </div>
        <div className="flex items-center space-x-2">
          <RadioGroupItem value="rail" id="rail" />
          <Label htmlFor="rail">Железнодорожная перевозка</Label>
        </div>
      </RadioGroup>
      <Button type="submit">Рассчитать</Button>
      {result && (
        <div className="mt-4 p-4 bg-blue-100 rounded">
          <p>Стоимость: {result.price} руб.</p>
          <p>Срок доставки: {result.duration} {result.duration === 1 ? 'день' : 'дня'}</p>
        </div>
      )}
    </form>
  )
}

