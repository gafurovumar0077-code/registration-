from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

pasw = os.getenv("PASSWORD_DB")

async def connection_db():
    try:
        conn = await asyncpg.connect(
            port=5432,
            host="localhost",
            user="postgres",
            database="task_db",
            password=pasw
        )
        print("Connection sucssesfull")
        return conn
    except Exception as error:
        print(f"Connection Error: {error}")

async def create_table():
    try:
        conn=await connection_db()
        await conn.execute("""
        Create table if not exists task(
            task_id serial primary key,
            titile varchar(200),
            description text,
            due_date varchar(50),
            status boolean default false,
            create_at timestamp default now(),
            is_active boolean default true
        )
                           """)
        print("Created table Succesful")
        return conn
    except Exception as error:
        print(f"Create table Error: {error}")
    finally:
        await conn.close()