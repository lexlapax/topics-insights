# Topic Insights Frontend

Next.js-based frontend for Topic Insights application.

## Repository

This is part of the [Topic Insights](https://github.com/lexlapax/topics-insights) project.

## Setup

1. **Clone Repository**:
```bash
git clone https://github.com/lexlapax/topics-insights.git
cd topics-insights/frontend
```

2. **Install Dependencies**:
```bash
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
- ✅ Git integration

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

## License

MIT
