import Image from 'next/image'
import Link from 'next/link'
import { Button } from '@/components/ui/button'
import CostCalculator from './components/cost-calculator'
import NewsSection from './components/news-section'

export default function Home() {
  return (
    <div className="space-y-16">
      {/* Hero Section */}
      <section className="relative h-[600px]">
        <Image
          src="/placeholder.svg?height=600&width=1200"
          alt="Логистические перевозки"
          fill
          style={{objectFit: "cover"}}
          priority
        />
        <div className="absolute inset-0 bg-blue-900 bg-opacity-70 flex items-center justify-center">
          <div className="text-center text-white">
            <h1 className="text-6xl font-bold mb-4">LogiTrans - Ваш надежный партнер в логистике</h1>
            <p className="text-2xl mb-8">Быстрые и надежные автомобильные и железнодорожные перевозки</p>
            <div className="space-x-4">
              <Button asChild className="bg-yellow-500 hover:bg-yellow-600 text-blue-900">
                <Link href="#about">Узнать больше</Link>
              </Button>
              <Button asChild variant="outline" className="text-yellow-500 border-yellow-500 hover:bg-yellow-500 hover:text-blue-900">
                <Link href="#calculator">Рассчитать стоимость</Link>
              </Button>
              <Button asChild variant="secondary" className="bg-white text-blue-900 hover:bg-gray-100">
                <Link href="/contacts">Связаться с нами</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-12 text-blue-900">О нашей компании</h2>
        <div className="grid md:grid-cols-3 gap-12">
          <div className="text-center">
            <Image src="/placeholder.svg?height=200&width=200" alt="Скорость" width={200} height={200} className="mx-auto mb-4 rounded-full" />
            <h3 className="text-2xl font-semibold mb-4 text-blue-700">Скорость</h3>
            <p className="text-gray-700">Мы гарантируем быструю доставку вашего груза в любую точку страны.</p>
          </div>
          <div className="text-center">
            <Image src="/placeholder.svg?height=200&width=200" alt="Надежность" width={200} height={200} className="mx-auto mb-4 rounded-full" />
            <h3 className="text-2xl font-semibold mb-4 text-blue-700">Надежность</h3>
            <p className="text-gray-700">Ваш груз в надежных руках. Мы обеспечиваем сохранность на всем пути следования.</p>
          </div>
          <div className="text-center">
            <Image src="/placeholder.svg?height=200&width=200" alt="Широкий охват" width={200} height={200} className="mx-auto mb-4 rounded-full" />
            <h3 className="text-2xl font-semibold mb-4 text-blue-700">Широкий охват</h3>
            <p className="text-gray-700">Наша сеть охватывает всю страну, обеспечивая доставку в самые отдаленные уголки.</p>
          </div>
        </div>
      </section>

      {/* Cost Calculator Section */}
      <section id="calculator" className="bg-blue-100 py-16">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-12 text-blue-900">Рассчитать стоимость перевозки</h2>
          <CostCalculator />
        </div>
      </section>

      {/* News Section */}
      <section className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-12 text-blue-900">Новости логистики</h2>
        <NewsSection />
      </section>
    </div>
  )
}

