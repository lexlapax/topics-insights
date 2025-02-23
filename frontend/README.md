# Topic Insights Frontend

Next.js-based frontend for Topic Insights application.

## Current State (2024-03-XX)
- ✅ Initial cleanup and dependency optimization
- ✅ Next.js 14.1.0 setup with App Router
- ✅ React Query v5 integration
- ✅ Chakra UI v2 setup
- ✅ Jest + React Testing Library configuration
- ✅ All tests passing with coverage
- ✅ Documentation updated to reflect current state

## Prerequisites

- Node.js 20.x (LTS)
- npm or yarn
- git

## Quick Start

1. **Install Dependencies**:
```bash
npm install
```

2. **Run Tests**:
```bash
# Run all tests with coverage
npm run test:coverage

# Run tests in watch mode
npm run test:watch
```

3. **Start Development Server**:
```bash
npm run dev
```

Visit `http://localhost:3000` to see the application.

## Project Structure

```
frontend/
├── __tests__/              # Test files
├── src/
│   └── app/               # Next.js App Router
│       ├── layout.tsx     # Root layout
│       ├── page.tsx       # Home page
│       └── providers.tsx  # App providers
├── jest.config.js         # Jest configuration
├── next.config.js         # Next.js configuration
└── package.json          # Project configuration
```

## Available Scripts

```bash
# Development
npm run dev         # Start development server
npm run build      # Build production bundle
npm run start      # Start production server

# Testing
npm run test       # Run tests
npm run test:watch # Run tests in watch mode
npm run test:coverage # Run tests with coverage

# Code Quality
npm run lint       # Run ESLint
npm run format     # Run Prettier
npm run type-check # Run TypeScript checks
```

## Development Tools

### Code Quality
```bash
# Format code
npm run format

# Lint code
npm run lint

# Type check
npm run type-check
```

### Testing
```bash
# Run all tests
npm run test

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm run test __tests__/page.test.tsx
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
# Run tests
npm run test
# Format and lint
npm run format
npm run lint
# Commit
git add .
git commit -m "feat: your frontend feature description"
```

4. **Push Changes**:
```bash
git push origin feature/frontend-feature-name
```

5. **Create Pull Request** on GitHub

## Troubleshooting

### Common Issues

1. **Wrong Node Version**
```bash
# Check version
node --version

# If incorrect, install Node.js 20.x LTS
```

2. **Module Resolution Issues**
```bash
# Clean install
rm -rf node_modules .next
npm install
```

3. **Test Failures**
```bash
# Run with verbose output
npm run test -- --verbose

# Run specific test
npm run test __tests__/page.test.tsx
```

4. **Development Server Issues**
```bash
# Check port
lsof -i :3000  # On Unix/macOS
netstat -ano | findstr :3000  # On Windows

# Start with different port
npm run dev -- -p 3001
```

## License

MIT
