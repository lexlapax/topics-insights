import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import Home from '@/app/page'
import { Providers } from '@/app/providers'

// Mock React Query
jest.mock('@tanstack/react-query', () => ({
  ...jest.requireActual('@tanstack/react-query'),
  useQuery: jest.fn().mockReturnValue({
    data: {
      status: 'ok',
      version: '0.1.0',
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

  it('displays system status', () => {
    render(
      <Providers>
        <Home />
      </Providers>
    )
    
    expect(screen.getByText(/Status: ok/i)).toBeInTheDocument()
  })
}) 