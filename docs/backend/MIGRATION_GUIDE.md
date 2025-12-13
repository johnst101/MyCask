# Database Migration Guide

This guide covers how to use Alembic for database migrations in the MyCask backend application.

## Overview

MyCask uses [Alembic](https://alembic.sqlalchemy.org/) for database schema migrations. Alembic is a database migration tool for SQLAlchemy that allows you to version control your database schema changes.

### Key Files

- **`backend/alembic.ini`** - Alembic configuration file
- **`backend/alembic/env.py`** - Migration environment script (loads models, configures database connection)
- **`backend/alembic/versions/`** - Directory containing migration scripts
- **`backend/app/db/database.py`** - Database connection configuration
- **`backend/app/models/`** - SQLAlchemy model definitions

## Prerequisites

1. **Database Setup**: Ensure PostgreSQL is running and accessible
2. **Environment Variables**: Set `DATABASE_URL` in your `.env` file:
   ```
   DATABASE_URL=postgresql://mycask:mycask123@localhost:5432/mycask
   ```
3. **Virtual Environment**: Activate your virtual environment:
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Common Migration Commands

### Check Current Migration Status

```bash
alembic current
```

Shows the current revision ID of the database.

### View Migration History

```bash
alembic history
```

Shows all available migrations in chronological order.

### View Migration History (Verbose)

```bash
alembic history --verbose
```

Shows detailed information about each migration.

## Creating Migrations

### Auto-generate Migration from Model Changes

When you modify SQLAlchemy models, Alembic can automatically detect changes:

```bash
alembic revision --autogenerate -m "Description of changes"
```

**Example:**

```bash
alembic revision --autogenerate -m "Add mashbill_description to bottles table"
```

**Important Notes:**

- Always review the generated migration file before applying it
- Alembic may not detect all changes (e.g., table renames, data migrations)
- Make sure all model files are imported in `alembic/env.py` so Alembic can detect them

### Create Empty Migration (Manual)

For complex changes or data migrations:

```bash
alembic revision -m "Description of changes"
```

This creates an empty migration file where you can write custom upgrade/downgrade logic.

## Running Migrations

### Apply All Pending Migrations

```bash
alembic upgrade head
```

Applies all migrations up to the latest version.

### Apply Specific Migration

```bash
alembic upgrade <revision_id>
```

Example:

```bash
alembic upgrade d4e5ac8c78d7
```

### Upgrade One Step

```bash
alembic upgrade +1
```

Applies the next migration in the sequence.

### Downgrade One Step

```bash
alembic downgrade -1
```

Reverts the most recent migration.

### Downgrade to Specific Revision

```bash
alembic downgrade <revision_id>
```

### Downgrade All Migrations

```bash
alembic downgrade base
```

⚠️ **Warning**: This will remove all tables. Use with caution!

## Migration Workflow

### Typical Development Workflow

1. **Modify Models**: Update SQLAlchemy models in `backend/app/models/`
2. **Generate Migration**:
   ```bash
   alembic revision --autogenerate -m "Your change description"
   ```
3. **Review Migration**: Check the generated file in `backend/alembic/versions/`
4. **Test Migration**: Apply to development database:
   ```bash
   alembic upgrade head
   ```
5. **Verify**: Check that tables/columns were created/modified correctly
6. **Commit**: Add migration file to version control

### Example: Adding a New Column

1. Edit `backend/app/models/bottle.py`:

   ```python
   class Bottle(Base):
       # ... existing columns ...
       new_field = Column(String(100), nullable=True)
   ```

2. Generate migration:

   ```bash
   alembic revision --autogenerate -m "Add new_field to bottles"
   ```

3. Review `backend/alembic/versions/xxxx_add_new_field_to_bottles.py`

4. Apply migration:
   ```bash
   alembic upgrade head
   ```

## How Alembic Detects Changes

Alembic compares:

- **Current Database Schema** (from `alembic_version` table)
- **Model Definitions** (from SQLAlchemy models imported in `env.py`)

### Model Import Configuration

All models must be imported in `backend/alembic/env.py`:

```python
from app.models import (
    user,
    bottle,
    user_bottle,
    bottle_purchase,
    bottle_prices,
    tasting,
    tasting_flavors,
    flavor_tags,
    wishlist
)
```

**When adding a new model:**

1. Create the model file in `backend/app/models/`
2. Add the import to `backend/alembic/env.py`
3. Generate a new migration

## Database Connection

The database URL is loaded from environment variables in `alembic/env.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL", "postgresql://mycask:mycask123@localhost:5432/mycask")
config.set_main_option("sqlalchemy.url", database_url)
```

This ensures Alembic uses the same database connection as your application.

## Best Practices

### 1. Always Review Auto-generated Migrations

Auto-generated migrations may need manual adjustments:

- Check for correct column types
- Verify foreign key constraints
- Ensure indexes are created correctly
- Add data migrations if needed

### 2. Use Descriptive Migration Messages

```bash
# Good
alembic revision --autogenerate -m "Add user profile picture URL"

# Bad
alembic revision --autogenerate -m "update"
```

### 3. Test Migrations Before Committing

Always test migrations on a development database before applying to production.

### 4. Keep Migrations Small and Focused

One logical change per migration makes it easier to:

- Review changes
- Debug issues
- Rollback if needed

### 5. Never Edit Applied Migrations

Once a migration has been applied to production, don't modify it. Create a new migration instead.

### 6. Backup Before Major Migrations

Before running migrations that modify large tables or drop columns:

```bash
# Create database backup
pg_dump -U mycask mycask > backup_$(date +%Y%m%d).sql
```

## Troubleshooting

### Issue: "Target database is not up to date"

**Error:**

```
ERROR [alembic.util.messaging] Target database is not up to date
```

**Solution:**

```bash
alembic upgrade head
```

### Issue: "Can't locate revision identified by 'xxxx'"

**Error:**

```
Can't locate revision identified by 'xxxx'
```

**Solution:**

- Check migration history: `alembic history`
- Verify migration files exist in `backend/alembic/versions/`
- Ensure you're on the correct branch if using Git

### Issue: "ImportError: cannot import name 'Decimal'"

**Error:**

```
ImportError: cannot import name 'Decimal' from 'sqlalchemy'
```

**Solution:**
Use `Numeric` instead of `Decimal` in model imports:

```python
from sqlalchemy import Column, Integer, String, Numeric  # Not Decimal
```

### Issue: "Could not parse SQLAlchemy URL"

**Error:**

```
sqlalchemy.exc.ArgumentError: Could not parse SQLAlchemy URL
```

**Solution:**

- Verify `DATABASE_URL` is set in `.env` file
- Check that `alembic/env.py` loads environment variables correctly
- Ensure database URL format is correct: `postgresql://user:password@host:port/database`

### Issue: Models Not Detected

**Problem:** Alembic doesn't detect model changes.

**Solution:**

1. Ensure model file is imported in `alembic/env.py`
2. Check that model inherits from `Base` (from `app.db.database`)
3. Verify model has `__tablename__` defined
4. Restart terminal/shell and try again

### Issue: Migration Conflicts

If multiple developers create migrations simultaneously:

1. **Pull latest changes:**

   ```bash
   git pull
   ```

2. **Check current database state:**

   ```bash
   alembic current
   ```

3. **Apply missing migrations:**

   ```bash
   alembic upgrade head
   ```

4. **If conflicts exist:** Merge migration files manually, ensuring proper `down_revision` chains

## Migration File Structure

A typical migration file looks like:

```python
"""Add new column

Revision ID: abc123def456
Revises: xyz789
Create Date: 2025-11-30 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers
revision: str = 'abc123def456'
down_revision: Union[str, None] = 'xyz789'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Apply migration."""
    op.add_column('bottles', sa.Column('new_field', sa.String(100), nullable=True))

def downgrade() -> None:
    """Revert migration."""
    op.drop_column('bottles', 'new_field')
```

## Advanced Topics

### Data Migrations

For migrating data (not just schema):

```python
def upgrade() -> None:
    # Schema change
    op.add_column('users', sa.Column('full_name', sa.String(255)))

    # Data migration
    connection = op.get_bind()
    connection.execute(
        sa.text("UPDATE users SET full_name = first_name || ' ' || last_name")
    )

def downgrade() -> None:
    op.drop_column('users', 'full_name')
```

### Conditional Migrations

```python
def upgrade() -> None:
    # Check if column exists before adding
    inspector = sa.inspect(op.get_bind())
    columns = [col['name'] for col in inspector.get_columns('bottles')]

    if 'new_field' not in columns:
        op.add_column('bottles', sa.Column('new_field', sa.String(100)))
```

### Custom SQL

```python
def upgrade() -> None:
    op.execute("CREATE INDEX CONCURRENTLY idx_bottles_name ON bottles(name)")
```

## Resources

- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Quick Reference

| Command                                    | Description                                         |
| ------------------------------------------ | --------------------------------------------------- |
| `alembic current`                          | Show current database revision                      |
| `alembic history`                          | Show migration history                              |
| `alembic revision --autogenerate -m "msg"` | Auto-generate migration                             |
| `alembic revision -m "msg"`                | Create empty migration                              |
| `alembic upgrade head`                     | Apply all pending migrations                        |
| `alembic upgrade +1`                       | Apply next migration                                |
| `alembic downgrade -1`                     | Revert last migration                               |
| `alembic downgrade base`                   | Remove all migrations                               |
| `alembic stamp head`                       | Mark database as current without running migrations |
