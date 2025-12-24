class Flight:
    """Class to represent a flight with all its details"""
    def __init__(self, flight_id, airline, source, destination, fare, duration, departure_time):
        self.flight_id = flight_id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.fare = fare
        self.duration = duration
        self.departure_time = departure_time
    
    def __str__(self):
        return f"{self.flight_id:8} | {self.airline:15} | {self.source:10} -> {self.destination:10} | ${self.fare:7.2f} | {self.duration:5} | {self.departure_time}"


class MinHeap:
    """Min Heap implementation for sorting flights by fare"""
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, flight):
        """Insert a flight into the heap"""
        self.heap.append(flight)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Maintain heap property upwards"""
        while i > 0 and self.heap[self.parent(i)].fare > self.heap[i].fare:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_min(self):
        """Remove and return the flight with minimum fare"""
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_flight = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_flight
    
    def _heapify_down(self, i):
        """Maintain heap property downwards"""
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left].fare < self.heap[min_idx].fare:
            min_idx = left
        
        if right < len(self.heap) and self.heap[right].fare < self.heap[min_idx].fare:
            min_idx = right
        
        if min_idx != i:
            self.swap(i, min_idx)
            self._heapify_down(min_idx)
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0


class AirlineFareComparator:
    """Main class for airline fare comparison system"""
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        """Add a flight to the system"""
        self.flights.append(flight)
    
    def heap_sort_by_fare(self):
        """Sort flights by fare using heap sort (ascending order)"""
        heap = MinHeap()
        
        # Insert all flights into the heap
        for flight in self.flights:
            heap.insert(flight)
        
        # Extract flights from heap to get sorted order
        sorted_flights = []
        while not heap.is_empty():
            sorted_flights.append(heap.extract_min())
        
        return sorted_flights
    
    def search_flights(self, source, destination):
        """Search flights between source and destination"""
        matching_flights = [f for f in self.flights 
                          if f.source.lower() == source.lower() 
                          and f.destination.lower() == destination.lower()]
        
        if not matching_flights:
            return []
        
        # Sort matching flights by fare using heap sort
        heap = MinHeap()
        for flight in matching_flights:
            heap.insert(flight)
        
        sorted_flights = []
        while not heap.is_empty():
            sorted_flights.append(heap.extract_min())
        
        return sorted_flights
    
    def get_cheapest_flight(self, source, destination):
        """Get the cheapest flight between two cities"""
        flights = self.search_flights(source, destination)
        return flights[0] if flights else None
    
    def display_flights(self, flights):
        """Display flights in a formatted table"""
        if not flights:
            print("No flights found!")
            return
        
        print("\n" + "="*100)
        print(f"{'Flight ID':8} | {'Airline':15} | {'Route':25} | {'Fare':9} | {'Duration':5} | {'Departure'}")
        print("="*100)
        for flight in flights:
            print(flight)
        print("="*100 + "\n")


def get_flight_input():
    """Get flight details from user"""
    print("\n--- Enter Flight Details ---")
    flight_id = input("Flight ID: ").strip()
    airline = input("Airline Name: ").strip()
    source = input("Source City: ").strip()
    destination = input("Destination City: ").strip()
    
    while True:
        try:
            fare = float(input("Fare (in $): ").strip())
            if fare <= 0:
                print("Fare must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid fare. Please enter a number.")
    
    duration = input("Duration (e.g., 2h 15m): ").strip()
    departure_time = input("Departure Time (e.g., 08:30 AM): ").strip()
    
    return Flight(flight_id, airline, source, destination, fare, duration, departure_time)


def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("AIRLINE FARE COMPARATOR SYSTEM")
    print("Using Heap Sort Algorithm")
    print("="*50)
    print("\n1. Add Flight")
    print("2. Display All Flights (Sorted by Fare)")
    print("3. Search Flights (Source to Destination)")
    print("4. Find Cheapest Flight")
    print("5. Exit")
    print("="*50)


def main():
    comparator = AirlineFareComparator()
    
    print("\n" + "="*50)
    print("WELCOME TO AIRLINE FARE COMPARATOR")
    print("="*50)
    
    # Option to load sample data
    choice = input("\nDo you want to load sample flight data? (yes/no): ").strip().lower()
    
    if choice in ['yes', 'y']:
        sample_flights = [
            Flight("AI101", "Air India", "Delhi", "Mumbai", 4500.00, "2h 15m", "06:00 AM"),
            Flight("SG202", "SpiceJet", "Delhi", "Mumbai", 3200.00, "2h 20m", "08:30 AM"),
            Flight("IN303", "IndiGo", "Delhi", "Mumbai", 2800.00, "2h 10m", "10:00 AM"),
            Flight("AI104", "Air India", "Delhi", "Mumbai", 5200.00, "2h 05m", "02:00 PM"),
            Flight("GO505", "GoAir", "Delhi", "Mumbai", 3100.00, "2h 25m", "04:30 PM"),
            Flight("AI201", "Air India", "Mumbai", "Bangalore", 5500.00, "1h 45m", "07:00 AM"),
            Flight("IN402", "IndiGo", "Mumbai", "Bangalore", 3500.00, "1h 50m", "09:00 AM"),
            Flight("SG503", "SpiceJet", "Mumbai", "Bangalore", 3000.00, "1h 55m", "11:30 AM"),
            Flight("AI301", "Air India", "Delhi", "Bangalore", 6200.00, "2h 45m", "06:30 AM"),
            Flight("IN604", "IndiGo", "Delhi", "Bangalore", 4100.00, "2h 50m", "08:00 AM"),
        ]
        for flight in sample_flights:
            comparator.add_flight(flight)
        print(f"\n✓ Loaded {len(sample_flights)} sample flights successfully!")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Add Flight
            flight = get_flight_input()
            comparator.add_flight(flight)
            print("\n✓ Flight added successfully!")
        
        elif choice == '2':
            # Display All Flights Sorted by Fare
            if not comparator.flights:
                print("\n✗ No flights available. Please add flights first.")
            else:
                print("\n--- ALL FLIGHTS SORTED BY FARE (Cheapest First) ---")
                sorted_flights = comparator.heap_sort_by_fare()
                comparator.display_flights(sorted_flights)
        
        elif choice == '3':
            # Search Flights
            if not comparator.flights:
                print("\n✗ No flights available. Please add flights first.")
            else:
                source = input("\nEnter Source City: ").strip()
                destination = input("Enter Destination City: ").strip()
                
                flights = comparator.search_flights(source, destination)
                
                if flights:
                    print(f"\n--- FLIGHTS FROM {source.upper()} TO {destination.upper()} ---")
                    comparator.display_flights(flights)
                else:
                    print(f"\n✗ No flights found from {source} to {destination}")
        
        elif choice == '4':
            # Find Cheapest Flight
            if not comparator.flights:
                print("\n✗ No flights available. Please add flights first.")
            else:
                source = input("\nEnter Source City: ").strip()
                destination = input("Enter Destination City: ").strip()
                
                cheapest = comparator.get_cheapest_flight(source, destination)
                
                if cheapest:
                    print(f"\n--- CHEAPEST FLIGHT FROM {source.upper()} TO {destination.upper()} ---")
                    print("\n" + "="*100)
                    print(f"{'Flight ID':8} | {'Airline':15} | {'Route':25} | {'Fare':9} | {'Duration':5} | {'Departure'}")
                    print("="*100)
                    print(cheapest)
                    print("="*100)
                    
                    # Show savings
                    all_flights = comparator.search_flights(source, destination)
                    if len(all_flights) > 1:
                        max_fare = max(f.fare for f in all_flights)
                        savings = max_fare - cheapest.fare
                        print(f"\n💰 You save ${savings:.2f} compared to the most expensive option!")
                else:
                    print(f"\n✗ No flights found from {source} to {destination}")
        
        elif choice == '5':
            # Exit
            print("\n" + "="*50)
            print("Thank you for using Airline Fare Comparator!")
            print("Heap Sort Algorithm - O(n log n) Time Complexity")
            print("="*50 + "\n")
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-5.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()