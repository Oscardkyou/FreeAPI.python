import Link from 'next/link'

export default function Footer() {
  return (
    <footer className="bg-blue-900 text-white">
      <div className="container mx-auto px-6 py-8">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/4 mb-6 md:mb-0">
            <h2 className="text-yellow-500 text-lg font-semibold mb-4">LogiTrans</h2>
            <p>Ваш надежный партнер в логистике</p>
          </div>
          <div className="w-full md:w-1/4 mb-6 md:mb-0">
            <h3 className="text-gray-900 font-semibold mb-4">Быстрые ссылки</h3>
            <ul className="space-y-2">
              <li><Link href="/" className="hover:text-yellow-500">Главная</Link></li>
              <li><Link href="/news" className="hover:text-yellow-500">Новости</Link></li>
              <li><Link href="/order" className="hover:text-yellow-500">Заказать</Link></li>
              <li><Link href="/contacts" className="hover:text-yellow-500">Контакты</Link></li>
            </ul>
          </div>
          <div className="w-full md:w-1/4 mb-6 md:mb-0">
            <h3 className="text-gray-900 font-semibold mb-4">Контакты</h3>
            <p>Email: info@logitrans.ru</p>
            <p>Телефон: +7 (999) 123-45-67</p>
          </div>
          <div className="w-full md:w-1/4">
            <h3 className="text-gray-900 font-semibold mb-4">Подписаться на новости</h3>
            <form className="flex">
              <input type="email" placeholder="Ваш email" className="rounded-l-lg p-2 border-t border-b border-l text-gray-800 border-gray-200 bg-white" />
              <button className="px-4 rounded-r-lg bg-yellow-500 text-blue-900 font-semibold p-2 uppercase border-yellow-500 border-t border-b border-r hover:bg-yellow-600">Подписаться</button>
            </form>
          </div>
        </div>
        <div className="border-t border-blue-800 mt-8 pt-8 text-center">
          <p>&copy; 2023 LogiTrans. Все права защищены.</p>
        </div>
      </div>
    </footer>
  )
}

