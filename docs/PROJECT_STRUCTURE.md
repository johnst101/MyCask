# Project Structure

## Directory Tree

```
MyCask/
├── backend/                    # FastAPI backend application
│   ├── app/                    # Main application package
│   │   ├── __init__.py
│   │   ├── main.py             # Application entry point
│   │   ├── __pycache__/        # Python cache files
│   │   ├── api/                # API route handlers
│   │   │   └── __init__.py
│   │   ├── db/                 # Database configuration & utilities
│   │   │   ├── __init__.py
│   │   │   └── database.py     # Database connection & setup
│   │   ├── models/             # SQLAlchemy ORM models
│   │   │   └── __init__.py
│   │   └── schemas/            # Pydantic request/response schemas
│   │       └── __init__.py
│   ├── services/               # Business logic & service layer
│   │   └── __init__.py
│   ├── requirements.txt        # Python dependencies
│   └── test_db.py              # Database testing utilities
│
├── frontend/                   # React + Vite frontend application
│   ├── public/                 # Static assets served publicly
│   ├── src/                    # Source code
│   │   ├── assets/             # Images, fonts, and other media
│   │   ├── components/         # Reusable React components
│   │   ├── pages/              # Page-level React components
│   │   ├── services/           # API client services
│   │   ├── hooks/              # Custom React hooks
│   │   ├── utils/              # Utility functions
│   │   ├── App.jsx             # Root component
│   │   ├── App.css             # Global styles
│   │   ├── main.jsx            # Application entry point
│   │   └── index.css           # Base styles
│   ├── index.html              # HTML entry point
│   ├── package.json            # Node.js dependencies & scripts
│   ├── vite.config.js          # Vite configuration
│   ├── eslint.config.js        # ESLint rules
│   └── README.md               # Frontend-specific documentation
│
├── docs/                       # Project documentation
│   ├── PROJECT_STRUCTURE.md    # This file
│   └── TECH_STACK.md           # Technology stack details
│
├── LICENSE                     # License file
├── README.md                   # Project overview & setup instructions
├── mycask_roadmap.md           # Project roadmap & milestones
└── MyCask.code-workspace       # VS Code workspace configuration
```

## Folder Purposes

### Root Level

- **backend/** - Contains the FastAPI REST API server handling all business logic and database operations
- **frontend/** - Contains the React + Vite web application for the user interface
- **docs/** - Documentation for the project including architecture and technical stack
- **LICENSE** - Open-source license (if applicable)
- **README.md** - Main project overview and quick start guide
- **mycask_roadmap.md** - Project planning document with features and milestones
- **MyCask.code-workspace** - VS Code workspace settings for the monorepo

### Backend (`/backend`)

- **app/main.py** - FastAPI application initialization and server startup
- **app/api/** - API route definitions and endpoint handlers
- **app/db/** - Database connection management and initialization
- **app/models/** - SQLAlchemy ORM models representing database tables
- **app/schemas/** - Pydantic data validation schemas for request/response serialization
- **app/services/** - Business logic layer separating concerns from routes
- **requirements.txt** - Python package dependencies (pip format)
- **test_db.py** - Database testing and initialization scripts

### Frontend (`/frontend`)

- **src/components/** - Reusable React components (buttons, cards, forms, etc.)
- **src/pages/** - Full-page components representing different routes
- **src/services/** - API client functions for backend communication
- **src/hooks/** - Custom React hooks for shared logic
- **src/utils/** - Helper functions and utilities
- **src/assets/** - Static media files (images, icons, fonts)
- **public/** - Static files served at root (favicon, manifest, etc.)
- **vite.config.js** - Vite build tool configuration
- **eslint.config.js** - Code quality and linting rules
- **package.json** - NPM scripts and frontend dependencies

### Documentation (`/docs`)

- **PROJECT_STRUCTURE.md** - Overview of the project directory structure
- **TECH_STACK.md** - Technology decisions and framework details
