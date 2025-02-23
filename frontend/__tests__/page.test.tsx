import { render, screen } from '@testing-library/react'
import Home from '@/app/page'
import { Providers } from '@/app/providers'

// Mock the useQuery hook
jest.mock('@tanstack/react-query', () => ({
  useQuery: () => ({
    data: {
      status: 'ok',
      version: '0.1.0',
      services: {
        api: 'healthy',
        database: 'not_configured',
        llm: 'not_configured',
      },
    },
    isLoading: false,
    error: null,
  }),
}))

describe('Home Page', () => {
  it('renders the main heading', () => {
    render(
      <Providers>
        <Home />
      </Providers>
    )
    
    expect(screen.getByRole('heading', { name: /Topic Insights/i })).toBeInTheDocument()
  })

  it('displays the health check information', () => {
    render(
      <Providers>
        <Home />
      </Providers>
    )
    
    expect(screen.getByText(/API Status:/i)).toBeInTheDocument()
    expect(screen.getByText(/Database Status:/i)).toBeInTheDocument()
    expect(screen.getByText(/LLM Status:/i)).toBeInTheDocument()
  })
}) 