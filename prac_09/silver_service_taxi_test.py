from silver_service_taxi import SilverServiceTaxi

def main():
    """SilverServiceTaxi Test"""
    taxi = SilverServiceTaxi("Test Car", 100, 5)
    taxi.start_fare()  # Start a new fare
    taxi.drive(68)
    print(taxi)
    print(f"Total fare: ${taxi.get_fare():.2f}")

    taxi1 = SilverServiceTaxi("Another Test Car", 200, 2)  # Changed the name and initial fare
    taxi1.start_fare()  # Start a new fare
    taxi1.drive(18)
    print(taxi1)
    print(f"Total fare: ${taxi1.get_fare():.2f}")

if __name__ == '__main__':
    main()
