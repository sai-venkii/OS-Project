class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.response_time = -1
        self.waiting_time = 0

def display_gantt_chart(gantt_chart):
    print("Gantt Chart:")
    print("-" * 97)
    for item in gantt_chart:
        print("|", item, end=" ")
    print("|")
    print("-" * 97)

def multi_level_scheduling(processes):
    gantt_chart = []
    current_time = 0
    completed_processes = []

    while processes:
        # Select SJF process if available
        sjf_processes = [process for process in processes if process.priority == 'SJF' and process.arrival_time <= current_time]
        if sjf_processes:
            shortest_process = min(sjf_processes, key=lambda x: x.remaining_time)
            shortest_process.response_time = current_time - shortest_process.arrival_time if shortest_process.response_time == -1 else shortest_process.response_time
            shortest_process.start_time = current_time
            shortest_process.waiting_time = current_time - shortest_process.arrival_time
            current_time += shortest_process.remaining_time
            shortest_process.completion_time = current_time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            gantt_chart.extend([shortest_process.pid] * shortest_process.burst_time)
            completed_processes.append(shortest_process)
            processes.remove(shortest_process)
        else:
            # If no SJF process available, use FCFS
            fcfs_processes = [process for process in processes if process.priority == 'FCFS' and process.arrival_time <= current_time]
            if fcfs_processes:
                next_process = fcfs_processes[0]
                next_process.response_time = current_time - next_process.arrival_time if next_process.response_time == -1 else next_process.response_time
                next_process.start_time = current_time
                next_process.waiting_time = current_time - next_process.arrival_time
                current_time += next_process.remaining_time
                next_process.completion_time = current_time
                next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
                gantt_chart.extend([next_process.pid] * next_process.burst_time)
                completed_processes.append(next_process)
                processes.remove(next_process)
            else:
                current_time += 1  

    display_gantt_chart(gantt_chart)
    calculate_metrics(completed_processes)

def calculate_metrics(processes):
    total_completion_time = sum(process.completion_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    total_response_time = sum(process.response_time for process in processes)
    total_waiting_time = sum(process.waiting_time for process in processes)

    num_processes = len(processes)
    avg_completion_time = round((total_completion_time / num_processes),2)
    avg_turnaround_time = round((total_turnaround_time / num_processes),2)
    avg_response_time = round((total_response_time / num_processes),2)
    avg_waiting_time = round((total_waiting_time / num_processes),2)

    print("\nProcess Metrics:")
    print("-" * 70)
    print("PID\tCompletion Time\tTurnaround Time\tResponse Time\tWaiting Time")
    print("-" * 70)

    for process in processes:
        print(
            f"{process.pid}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.response_time}\t\t{process.waiting_time}"
        )

    print("-" * 70)

    print("\nAverage Metrics:")
    print("-" * 70)
    print(
        f"Average Completion Time: {avg_completion_time}\nAverage Turnaround Time: {avg_turnaround_time}\nAverage Response Time: {avg_response_time}\nAverage Waiting Time: {avg_waiting_time}"
    )
    print("-" * 70)

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(pid=1, arrival_time=0, burst_time=3, priority='FCFS'),
        Process(pid=2, arrival_time=1, burst_time=5, priority='SJF'),
        Process(pid=3, arrival_time=2, burst_time=4, priority='SJF'),
        Process(pid=4, arrival_time=3, burst_time=2, priority='FCFS'),
        Process(pid=5, arrival_time=4, burst_time=7, priority='SJF'),
        Process(pid=6, arrival_time=5, burst_time=3, priority='FCFS')
    ]

    multi_level_scheduling(processes)
