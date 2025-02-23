# Topic Insights Frontend

Next.js-based frontend for Topic Insights application.

## Repository

This is part of the [Topic Insights](https://github.com/lexlapax/topics-insights) project.

## Test-First Development Guide

### For Developers and AI Agents (Cursor, GitHub Copilot, etc.)

#### 1. Test File Creation
- Create test file BEFORE component file
- Test filename pattern: `*.test.tsx` or `*.spec.tsx`
- Place tests next to components:
  ```
  src/components/
    └── Feature/
        ├── Feature.tsx
        ├── Feature.test.tsx
        └── Feature.styles.ts
  ```

#### 2. Test Writing Sequence
1. Write imports and setup
2. Write test suite description
3. Write individual test cases
4. Add mock providers/context
5. Add test utilities
6. ONLY THEN proceed to implementation

Example:
```typescript
// components/TopicAnalysis/TopicAnalysis.test.tsx
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TopicAnalysis } from './TopicAnalysis'
import { QueryClientProvider } from '@tanstack/react-query'

describe('TopicAnalysis Component', () => {
  const mockAnalyzeHandler = jest.fn()
  
  beforeEach(() => {
    mockAnalyzeHandler.mockClear()
  })
  
  it('should render analysis form', () => {
    render(<TopicAnalysis onAnalyze={mockAnalyzeHandler} />)
    expect(screen.getByRole('textbox')).toBeInTheDocument()
    expect(screen.getByRole('button')).toHaveTextContent('Analyze')
  })
  
  it('should handle analysis submission', async () => {
    render(<TopicAnalysis onAnalyze={mockAnalyzeHandler} />)
    await userEvent.type(screen.getByRole('textbox'), 'test topic')
    await userEvent.click(screen.getByRole('button'))
    expect(mockAnalyzeHandler).toHaveBeenCalledWith('test topic')
  })
})
```

#### 3. AI Agent Guidelines

When using AI assistance (Cursor, GitHub Copilot):

1. **Test Request Format**
   ```
   Create tests for [component] that:
   - Test rendering
   - Test user interactions
   - Test async operations
   - Test error states
   - Mock API calls
   - Test accessibility
   ```

2. **Implementation Request Format**
   ```
   Implement [component] to pass these tests:
   [paste test code]
   Requirements:
   - Match test specifications
   - Handle loading/error states
   - Include TypeScript types
   - Follow accessibility guidelines
   - Add prop documentation
   ```

3. **Refactoring Request Format**
   ```
   Refactor [component] while maintaining test compliance:
   - Improve [specific aspect]
   - Maintain test coverage
   - Keep existing functionality
   - Enhance performance
   ```

#### 4. Test Categories

1. **Unit Tests**
   - Test individual components
   - Mock all external dependencies
   - Fast execution
   ```typescript
   it('should format date correctly', () => {
     render(<DateDisplay date="2024-02-23" />)
     expect(screen.getByText('Feb 23, 2024')).toBeInTheDocument()
   })
   ```

2. **Integration Tests**
   - Test component interactions
   - Test data flow
   - Mock API calls
   ```typescript
   it('should display analysis results', async () => {
     const mockApi = jest.fn().mockResolvedValue({ data: 'analysis' })
     render(
       <QueryClientProvider client={queryClient}>
         <TopicAnalysis api={mockApi} />
       </QueryClientProvider>
     )
     // Test interaction and results
   })
   ```

3. **E2E Tests**
   - Test complete user flows
   - Minimal mocking
   - Real API endpoints (in test environment)
   ```typescript
   test('complete topic analysis flow', async () => {
     await page.goto('/topics')
     await page.fill('[name="topic"]', 'AI trends')
     await page.click('button[type="submit"]')
     await expect(page.locator('.analysis-result')).toBeVisible()
   })
   ```

#### 5. Coverage Requirements

Minimum coverage requirements by component type:
- UI Components: 90%
- Hooks: 95%
- Utils: 85%
- API Clients: 80%
- Overall project: 85%

Check coverage:
```bash
npm test -- --coverage
```

#### 6. Test Performance

- Unit tests: < 50ms each
- Integration tests: < 500ms each
- E2E tests: < 30s each
- Run slow tests separately:
  ```bash
  npm run test:e2e
  ```

#### 7. Continuous Testing

```bash
# Watch mode for TDD
npm run test:watch

# Run specific test suites
npm test components
npm test hooks
npm test utils
```

#### 8. Mocking Guidelines

1. **API Calls**
```typescript
jest.mock('@/api', () => ({
  analyzeTopics: jest.fn().mockResolvedValue({
    data: { analysis: 'mocked result' }
  })
}))
```

2. **React Hooks**
```typescript
jest.mock('react-query', () => ({
  useQuery: jest.fn().mockReturnValue({
    data: mockData,
    isLoading: false,
    error: null
  })
}))
```

3. **Context Providers**
```typescript
const mockAuthContext = {
  user: { id: 1, name: 'Test' },
  isAuthenticated: true
}

render(
  <AuthContext.Provider value={mockAuthContext}>
    <Component />
  </AuthContext.Provider>
)
```

#### 9. Component Testing Checklist

- ✅ Renders without crashing
- ✅ Handles all prop variations
- ✅ Manages loading states
- ✅ Handles error states
- ✅ Processes user interactions
- ✅ Maintains accessibility
- ✅ Responsive behavior
- ✅ Performance metrics

#### 10. Testing Utilities

1. **Custom Renders**
```typescript
// test-utils.tsx
export const renderWithProviders = (
  ui: React.ReactElement,
  options = {}
) => {
  return render(
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        {ui}
      </ThemeProvider>
    </QueryClientProvider>,
    options
  )
}
```

2. **Common Assertions**
```typescript
// assertions.ts
export const expectLoading = () => {
  expect(screen.getByRole('progressbar')).toBeInTheDocument()
}

export const expectError = (message: string) => {
  expect(screen.getByRole('alert')).toHaveTextContent(message)
}
```

## Development Setup

1. **Clone Repository**:
```bash
git clone https://github.com/lexlapax/topics-insights.git
cd topics-insights/frontend
```

2. **Install Dependencies**:
```bash
# Use correct Node.js version
nvm use 18.17.0  # Install if needed: nvm install 18.17.0

# Install packages
npm install
```

3. **Development Server**:
```bash
npm run dev
```

The application will be available at http://localhost:3000

## Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── page.tsx        # Home page
│   │   ├── layout.tsx      # Root layout
│   │   └── providers.tsx   # App providers (React Query + Chakra UI)
│   └── components/         # Shared components
├── __tests__/             # Test files
├── public/                # Static files
├── package.json          # Project configuration
└── README.md            # This file
```

## Current Features

- ✅ Next.js 14.1.0 setup
- ✅ React Query v5 integration
- ✅ Chakra UI v2 integration
- ✅ TypeScript configuration
- ✅ Jest + React Testing Library setup
- ✅ ESLint + Prettier configuration
- ✅ Git integration

## TODO List

### High Priority
- [ ] Create authentication pages (login/register)
- [ ] Add topic creation form
- [ ] Implement topic list view
- [ ] Add error boundaries and loading states

### Medium Priority
- [ ] Add topic detail view
- [ ] Create reusable components
- [ ] Implement data caching
- [ ] Add form validation

### Low Priority
- [ ] Add dark mode support
- [ ] Implement keyboard shortcuts
- [ ] Add analytics tracking
- [ ] Create mobile-responsive design

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build production bundle
- `npm start` - Start production server
- `npm run lint` - Run ESLint
- `npm test` - Run tests
- `npm run test:watch` - Run tests in watch mode
- `npm run test:coverage` - Run tests with coverage

## Development Tools

- **Linting**:
```bash
npm run lint
```

- **Type Checking**:
```bash
# Run TypeScript compiler
tsc --noEmit
```

## Git Workflow

1. **Get Latest Code**:
```bash
git pull origin main
```

2. **Create Feature Branch**:
```bash
git checkout -b feature/frontend-feature-name
```

3. **Make Changes**:
```bash
# Make your changes
# Run tests
npm test
# Lint and type check
npm run lint
tsc --noEmit
# Commit
git add .
git commit -m "feat: your frontend feature description"
```

4. **Push Changes**:
```bash
git push origin feature/frontend-feature-name
```

5. **Create Pull Request**:
- Visit: https://github.com/lexlapax/topics-insights/pulls
- Click "New Pull Request"
- Select your feature branch
- Add description and request review

## Troubleshooting

- **Tests fail**: Verify Node.js version (18.17.0+)
- **Server won't start**: Check if port 3000 is in use
- **Module errors**: Run `npm install` again
- **Type errors**: Run `tsc --noEmit` to check types
- **Jest errors**: Check babel configuration and test setup

## License

MIT
