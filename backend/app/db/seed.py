'''
Seed the database with initial data.
'''

from app.db.database import SessionLocal
from app.models import User, UserBottle, BottlePrice, BottlePurchase, Bottle, Tasting, TastingFlavor, FlavorTag, Wishlist
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_database():
    db = SessionLocal()

    db.query(User).delete()
    db.query(UserBottle).delete()
    db.query(BottlePrice).delete()
    db.query(BottlePurchase).delete()
    db.query(Bottle).delete()
    db.query(Tasting).delete()
    db.query(TastingFlavor).delete()
    db.query(FlavorTag).delete()
    db.query(Wishlist).delete()

    db.commit()

    # Create users
    user1 = User(
        email="tylercjohnson16@gmail.com",
        password_hash=pwd_context.hash("password"),
        username="tyler.johnson"
    )
    user2 = User(
        email="chris.johnson@trimarq.com",
        password_hash=pwd_context.hash("password"),
        username="chris.johnson"
    )
    user3 = User(
        email="emily_johnson@comcast.net",
        password_hash=pwd_context.hash("password"),
        username="emily.johnson"
    )
    db.add(user1)
    db.add(user2)
    db.add(user3)
    db.commit()

    # Create bottles
    buffalo_trace = Bottle(
        name="Buffalo Trace",
        distillery="Buffalo Trace",
        type="Bourbon",
        region="Kentucky",
        age_years=10,
        abv=45.0,
        msrp=100.0,
        barcode="1234567890",
        description="A classic bourbon from Kentucky.",
    )
    ### TODO ### Add more bottles

if __name__ == "__main__":
    seed_database()
