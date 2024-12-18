import Link from 'next/link'
import { Button } from '@/components/ui/button'

export default function Header() {
  return (
    <header className="bg-blue-900 text-white shadow-md">
      <nav className="container mx-auto px-6 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-yellow-500">LogiTrans</Link>
          <div className="space-x-4">
            <Link href="/" className="text-white hover:text-yellow-500">Главная</Link>
            <Link href="/news" className="text-white hover:text-yellow-500">Новости</Link>
            <Link href="/order" className="text-white hover:text-yellow-500">Заказать</Link>
            <Link href="/contacts" className="text-white hover:text-yellow-500">Контакты</Link>
          </div>
        </div>
      </nav>
    </header>
  )
}

