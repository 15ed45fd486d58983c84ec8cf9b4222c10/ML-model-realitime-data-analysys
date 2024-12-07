import cityflow

engine = cityflow.Engine("config.json", thread_num=1)
engine.set_save_replay(True) 

try:
    for step in range(100):
        engine.next_step()
        print(f"Step {step + 1}: {engine.get_vehicle_count()} vehicles on the road")
except Exception as e:
    print(f"Error during simulation: {e}")
finally:
    print("Simulation completed.")
