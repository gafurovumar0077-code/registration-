from connection import *

async def create_task(title, descp, due_date):
    try:
        conn=await connection_db()
        await conn.execute("""
            insert into task(titile, description, due_date) values
            ($1, $2, $3)
                    """, title, descp, due_date)
        
        print("Creaetd task sucssesfull")
    except Exception as error:
        print(f"Create task Error: {error}")
    finally:
        await conn.close()

async def get_task():
    try:
        conn=await connection_db()
        tasks=await conn.fetch("""
            select * from task
                               """)
        for task in tasks:
            print(f"""
Task ID: {task["task_id"]}
Title: {task["titile"]}
Description: {task["description"]}
Dueration date: {task["due_date"]}
Status: {task["status"]}
Created at: {task["create_at"]}
                  """)
        return tasks
    except Exception as error:
        print(f"Get task Error: {error}")
    finally:
        await conn.close()