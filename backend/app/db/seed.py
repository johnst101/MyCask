'''
Seed the database with initial data.
'''

from app.db.database import SessionLocal
from app.models import User, UserBottle, BottlePrice, BottlePurchase, Bottle, Tasting, TastingFlavor, FlavorTag, Wishlist
from app.core.security import hash_password

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
        first_name="Tyler",
        last_name="Johnson",
        password_hash=hash_password("Password123!"),
        username="tyler.johnson"
    )
    user2 = User(
        email="chris.johnson@trimarq.com",
        first_name="Chris",
        last_name="Johnson",
        password_hash=hash_password("Password123!"),
        username="chris.johnson"
    )
    user3 = User(
        email="emily_johnson@comcast.net",
        first_name="Emily",
        last_name="Johnson",
        password_hash=hash_password("Password123!"),
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
        abv=45.00,
        msrp=35.00,
        barcode="1234567890",
        description="A classic bourbon from Kentucky.",
        mashbill_description="A classic bourbon from Kentucky.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    russells_reserve_10 = Bottle(
        name="Russell’s Reserve 10 Year",
        distillery="Wild Turkey",
        type="Bourbon",
        region="Kentucky, USA",
        age_years=10,
        abv=45.00,
        msrp=45.00,
        barcode="1002345678",
        description="Rich vanilla, caramel, and oak with balanced spice.",
        mashbill_description="~75% corn, 13% rye, 12% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    four_roses_small_batch = Bottle(
        name="Four Roses Small Batch",
        distillery="Four Roses",
        type="Bourbon",
        region="Kentucky, USA",
        age_years=7,
        abv=45.00,
        msrp=40.00,
        barcode="2009876543",
        description="Fruity, floral, and spicy blend of 4 recipes.",
        mashbill_description="Corn-heavy, high rye mashbill variants.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    sazerac_rye = Bottle(
        name="Sazerac Rye 100 Proof",
        distillery="Buffalo Trace",
        type="Rye",
        region="Kentucky, USA",
        age_years=6,
        abv=50.00,
        msrp=35.00,
        barcode="3001928374",
        description="Peppery spice, citrus, and vanilla sweetness.",
        mashbill_description="~51% rye, 39% corn, 10% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    elijah_craig_bp = Bottle(
        name="Elijah Craig Barrel Proof",
        distillery="Heaven Hill",
        type="Bourbon",
        region="Kentucky, USA",
        age_years=12,
        abv=63.00,
        msrp=70.00,
        barcode="4005647382",
        description="Intense oak, caramel, and baking spice.",
        mashbill_description="~75% corn, 13% rye, 12% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    green_spot = Bottle(
        name="Green Spot",
        distillery="Midleton",
        type="Irish Whiskey",
        region="Ireland",
        age_years=9,
        abv=40.00,
        msrp=65.00,
        barcode="5009182736",
        description="Apple, pear, and honey with light oak.",
        mashbill_description="Single pot still: malted & unmalted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    redbreast_12 = Bottle(
        name="Redbreast 12",
        distillery="Midleton",
        type="Irish Whiskey",
        region="Ireland",
        age_years=12,
        abv=40.00,
        msrp=70.00,
        barcode="6008372619",
        description="Full-bodied sherry influence, nutty and fruity.",
        mashbill_description="Pot still: malted & unmalted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    lagavulin_16 = Bottle(
        name="Lagavulin 16",
        distillery="Lagavulin",
        type="Scotch (Single Malt)",
        region="Islay, Scotland",
        age_years=16,
        abv=43.00,
        msrp=100.00,
        barcode="7005647381",
        description="Smoky peat, maritime salt, and dried fruit.",
        mashbill_description="100% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    macallan_12 = Bottle(
        name="Macallan 12 Sherry Oak",
        distillery="Macallan",
        type="Scotch (Single Malt)",
        region="Speyside, Scotland",
        age_years=12,
        abv=43.00,
        msrp=80.00,
        barcode="8009182736",
        description="Rich sherry sweetness, dried fruit, and spice.",
        mashbill_description="100% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    glenfiddich_12 = Bottle(
        name="Glenfiddich 12",
        distillery="Glenfiddich",
        type="Scotch (Single Malt)",
        region="Speyside, Scotland",
        age_years=12,
        abv=40.00,
        msrp=50.00,
        barcode="9008372619",
        description="Fresh pear, floral notes, and light oak.",
        mashbill_description="100% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    yamazaki_12 = Bottle(
        name="Yamazaki 12",
        distillery="Suntory",
        type="Japanese Single Malt",
        region="Japan",
        age_years=12,
        abv=43.00,
        msrp=150.00,
        barcode="1019283746",
        description="Complex fruit, honey, and subtle smoke.",
        mashbill_description="100% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    hibiki_harmony = Bottle(
        name="Hibiki Harmony",
        distillery="Suntory",
        type="Japanese Blend",
        region="Japan",
        age_years=0,
        abv=43.00,
        msrp=90.00,
        barcode="1128374650",
        description="Elegant blend of malt and grain whiskies.",
        mashbill_description="Blend of malted barley & grain.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    blantons_original = Bottle(
        name="Blanton’s Original",
        distillery="Buffalo Trace",
        type="Bourbon",
        region="Kentucky, USA",
        age_years=7,
        abv=46.50,
        msrp=65.00,
        barcode="1234567891",
        description="Vanilla, caramel, citrus, and spice.",
        mashbill_description="~70% corn, 16% rye, 14% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    woodford_reserve = Bottle(
        name="Woodford Reserve",
        distillery="Brown-Forman",
        type="Bourbon",
        region="Kentucky, USA",
        age_years=7,
        abv=45.20,
        msrp=40.00,
        barcode="1345678902",
        description="Rich caramel, chocolate, and spice.",
        mashbill_description="72% corn, 18% rye, 10% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    jack_daniels_no7 = Bottle(
        name="Jack Daniel’s Old No. 7",
        distillery="Jack Daniel’s",
        type="Tennessee Whiskey",
        region="Tennessee, USA",
        age_years=0,
        abv=40.00,
        msrp=25.00,
        barcode="1456789013",
        description="Smooth vanilla, banana, and charcoal mellow.",
        mashbill_description="80% corn, 8% rye, 12% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    makers_mark = Bottle(
        name="Maker’s Mark",
        distillery="Maker’s Mark",
        type="Bourbon (Wheated)",
        region="Kentucky, USA",
        age_years=6,
        abv=45.00,
        msrp=30.00,
        barcode="1567890124",
        description="Sweet caramel, vanilla, and soft wheat finish.",
        mashbill_description="70% corn, 16% wheat, 14% malted barley.",
        image_url="https://www.buffalotracedistillery.com/our-brands/buffalo-trace/_jcr_content/root/container/container_477176612/image.coreimg.100.1200.png/1756929640136/buffalo-desktop-bottle.png",
        is_variant=False,
        parent_bottle_id=None,
        barrel_number=None,
        warehouse=None,
        batch_number=None,
        vintage_year=None,
        proof_actual=None,
        age_statement_actual=None,
        pick_information=None,
        tier_run=None,
        bottle_date=None,
        release_info=None,
    )
    db.add(buffalo_trace)
    db.add(russells_reserve_10)
    db.add(four_roses_small_batch)
    db.add(sazerac_rye)
    db.add(elijah_craig_bp)
    db.add(green_spot)
    db.add(redbreast_12)
    db.add(lagavulin_16)
    db.add(macallan_12)
    db.add(glenfiddich_12)
    db.add(yamazaki_12)
    db.add(hibiki_harmony)
    db.add(blantons_original)
    db.add(woodford_reserve)
    db.add(jack_daniels_no7)
    db.add(makers_mark)
    db.commit()

    # Create flavor tags
    smoky = FlavorTag(name="smoky")
    spicy = FlavorTag(name="spicy")
    sweet = FlavorTag(name="sweet")
    fruity = FlavorTag(name="fruity")
    floral = FlavorTag(name="floral")
    herbal = FlavorTag(name="herbal")
    woody = FlavorTag(name="woody")
    nutty = FlavorTag(name="nutty")
    vanilla = FlavorTag(name="vanilla")
    caramel = FlavorTag(name="caramel")
    db.add(smoky)
    db.add(spicy)
    db.add(sweet)
    db.add(fruity)
    db.add(floral)
    db.add(herbal)
    db.add(woody)
    db.add(nutty)
    db.add(vanilla)
    db.add(caramel)
    db.commit()

    # Create user bottles
    user_bottle1 = UserBottle(
        user_id=user1.id,
        bottle_id=buffalo_trace.id,
        current_quantity=2
    )
    user_bottle2 = UserBottle(
        user_id=user1.id,
        bottle_id=russells_reserve_10.id,
        current_quantity=1
    )
    user_bottle3 = UserBottle(
        user_id=user1.id,
        bottle_id=four_roses_small_batch.id,
        current_quantity=3
    )
    user_bottle4 = UserBottle(
        user_id=user1.id,
        bottle_id=sazerac_rye.id,
        current_quantity=2
    )
    user_bottle5 = UserBottle(
        user_id=user2.id,
        bottle_id=green_spot.id,
        current_quantity=1
    )
    user_bottle6 = UserBottle(
        user_id=user2.id,
        bottle_id=redbreast_12.id,
        current_quantity=2
    )
    user_bottle7 = UserBottle(
        user_id=user2.id,
        bottle_id=lagavulin_16.id,
        current_quantity=1
    )
    user_bottle8 = UserBottle(
        user_id=user3.id,
        bottle_id=yamazaki_12.id,
        current_quantity=1
    )
    user_bottle9 = UserBottle(
        user_id=user3.id,
        bottle_id=hibiki_harmony.id,
        current_quantity=2
    )
    user_bottle10 = UserBottle(
        user_id=user3.id,
        bottle_id=blantons_original.id,
        current_quantity=1
    )
    user_bottle11 = UserBottle(
        user_id=user3.id,
        bottle_id=woodford_reserve.id,
        current_quantity=1
    )
    db.add(user_bottle1)
    db.add(user_bottle2)
    db.add(user_bottle3)
    db.add(user_bottle4)
    db.add(user_bottle5)
    db.add(user_bottle6)
    db.add(user_bottle7)
    db.add(user_bottle8)
    db.add(user_bottle9)
    db.add(user_bottle10)
    db.add(user_bottle11)
    db.commit()

if __name__ == "__main__":
    seed_database()
