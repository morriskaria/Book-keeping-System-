import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/billing': 'http://localhost:8000',
      '/auth': 'http://localhost:8000',
      '/expenses': 'http://localhost:8000',
      '/payroll': 'http://localhost:8000',
      '/inventory': 'http://localhost:8000',
      '/reports': 'http://localhost:8000',
      '/health': 'http://localhost:8000',
    }
  }
})
