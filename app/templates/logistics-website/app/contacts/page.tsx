'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import Image from 'next/image'

export default function ContactsPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
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
    alert('Сообщение отправлено!')
  }

  return (
    <div className="container mx-auto px-6 py-8">
      <h1 className="text-4xl font-bold mb-12 text-center text-blue-900">Контакты и отзывы</h1>
      
      <div className="grid md:grid-cols-2 gap-12">
        <div>
          <h2 className="text-3xl font-semibold mb-6 text-blue-800">Наши офисы</h2>
          <div className="space-y-6">
            <div className="bg-blue-100 p-6 rounded-lg shadow-md">
              <h3 className="font-semibold text-xl text-blue-900 mb-2">Москва</h3>
              <p className="text-blue-800">ул. Ленина, 123</p>
              <p className="text-blue-800">Тел: +7 (495) 123-45-67</p>
              <Image src="/placeholder.svg?height=200&width=300" alt="Офис в Москве" width={300} height={200} className="mt-4 rounded-lg" />
            </div>
            <div className="bg-blue-100 p-6 rounded-lg shadow-md">
              <h3 className="font-semibold text-xl text-blue-900 mb-2">Санкт-Петербург</h3>
              <p className="text-blue-800">Невский проспект, 456</p>
              <p className="text-blue-800">Тел: +7 (812) 987-65-43</p>
              <Image src="/placeholder.svg?height=200&width=300" alt="Офис в Санкт-Петербурге" width={300} height={200} className="mt-4 rounded-lg" />
            </div>
          </div>
          
          <div className="mt-12">
            <h2 className="text-3xl font-semibold mb-6 text-blue-800">Карта</h2>
            {/* Here you would typically embed a map */}
            <div className="bg-blue-100 h-64 flex items-center justify-center rounded-lg shadow-md">
              <Image src="/placeholder.svg?height=256&width=512" alt="Карта расположения офисов" width={512} height={256} className="rounded-lg" />
            </div>
          </div>
        </div>
        
        <div>
          <h2 className="text-3xl font-semibold mb-6 text-blue-800">Связаться с нами</h2>
          <form onSubmit={handleSubmit} className="space-y-6 bg-blue-100 p-6 rounded-lg shadow-md">
            <div>
              <Label htmlFor="name" className="text-blue-900">Имя</Label>
              <Input id="name" name="name" value={formData.name} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
            </div>
            <div>
              <Label htmlFor="email" className="text-blue-900">Email</Label>
              <Input id="email" name="email" type="email" value={formData.email} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
            </div>
            <div>
              <Label htmlFor="message" className="text-blue-900">Сообщение</Label>
              <Textarea id="message" name="message" value={formData.message} onChange={handleChange} required className="border-blue-300 focus:border-blue-500" />
            </div>
            <Button type="submit" className="bg-yellow-500 text-blue-900 hover:bg-yellow-600">Отправить</Button>
          </form>
          
          <div className="mt-12">
            <h2 className="text-3xl font-semibold mb-6 text-blue-800">Отзывы клиентов</h2>
            <div className="space-y-6">
              <div className="bg-blue-100 p-6 rounded-lg shadow-md">
                <p className="italic text-blue-800">"Отличный сервис! Груз доставлен вовремя и в целости."</p>
                <p className="text-right text-blue-900 mt-2">- Иван П.</p>
                <Image src="/placeholder.svg?height=100&width=100" alt="Фото клиента" width={100} height={100} className="rounded-full mt-4" />
              </div>
              <div className="bg-blue-100 p-6 rounded-lg shadow-md">
                <p className="italic text-blue-800">"Всегда пользуюсь услугами LogiTrans. Надежно и быстро."</p>
                <p className="text-right text-blue-900 mt-2">- Анна С.</p>
                <Image src="/placeholder.svg?height=100&width=100" alt="Фото клиента" width={100} height={100} className="rounded-full mt-4" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

