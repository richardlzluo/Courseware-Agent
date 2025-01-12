import asyncio

# Global variable to indicate when the task should stop
finished = False

# Background task function
async def background_task():
    while not finished:  # Keep running until 'finished' turns True
        print("Background task is running...")
        await asyncio.sleep(1)  # Simulate some work with a delay

    print("Background task has stopped.")

# Main function
async def main():
    global finished

    # Start the background task
    task = asyncio.create_task(background_task())

    # Simulate some other work in the main function
    for i in range(5):
        print(f"Main task iteration {i + 1}")
        await asyncio.sleep(2)

    # Set 'finished' to True to stop the background task
    finished = True

    # Wait for the background task to complete
    await task

    print("Main function is done.")

# Run the main function
asyncio.run(main())