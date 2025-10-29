export default function App() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="p-8 rounded-lg shadow-lg bg-white">
        <h1 className="text-2xl font-bold mb-4">React + Tailwind (dev)</h1>
        <p className="text-gray-700">This is a development build served by Vite inside Docker.</p>
        <p className="mt-4">Try calling the backend: <a className="text-blue-600" href="/api/health">/api/health</a></p>
      </div>
    </div>
  )
}
