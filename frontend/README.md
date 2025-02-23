# Topic Insights Frontend

Next.js-based frontend for Topic Insights application.

## Setup

1. **Install Dependencies**:
```bash
npm install
```

2. **Development Server**:
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
│   │   └── providers.tsx   # App providers
│   └── components/
├── __tests__/             # Test files
├── public/                # Static files
├── package.json          # Project configuration
└── README.md            # This file
```

## Current Features

- ✅ Next.js 14 setup
- ✅ React Query for data fetching
- ✅ Chakra UI for styling
- ✅ TypeScript configuration
- ✅ Jest + React Testing Library setup
- ✅ ESLint + Prettier configuration

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

1. **Initial Setup**:
```bash
git init
git add .
git commit -m "feat: Initial frontend setup"
```

2. **Development**:
```bash
git checkout -b feature/your-feature
# Make changes
git add .
git commit -m "feat: Add your feature"
```

## License

MIT
