import unittest
from route_analyzer import RouteAnalyzer


class Test(unittest.TestCase):

    def test_ConstructorShouldNotCrash(self):
        ''' (1) tests that the constructor does not throw an exception '''

        try:
            ra = RouteAnalyzer()
            crash = False
        except:
            crash = True

        self.assertFalse(
            crash, 'The route analyzer crashed in the constructor.')

    def test_AddAirport(self):
        '''bug 2: parameter dirty is not used'''
        ra = RouteAnalyzer()
        # ra.printState()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        airport = ra._airports[0]
        self.assertEqual(len(airport), 5, "Airport should contains 5 elements")

    def test_CanIFlyThereWithInfiniteLoop(self):
        '''bug 3: when there is no path between departure airport and arrival airport,
        method can_I_fly_there went into infinite loop'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        self.assertFalse(ra.can_I_fly_there('SDO', 'SNA'))
        self.assertFalse(ra.can_I_fly_there('SDO', 'JFK'))

    def test_CanIFlyThereShouldNotCrash(self):
        '''bug 4: tests that the can_I_fly_there does not throw an exception'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        try:
            ra.can_I_fly_there('SNA', 'JFK')
            ra.can_I_fly_there('SNA', 'DCA')
            crash = False
        except:
            crash = True
        self.assertFalse(
            crash, "The route analyzer crashed in the can_I_fly_there.")

    def test_CheapestRouteRightDirection(self):
        '''bug 5: the direction of the cheapest route should be right'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        res = ra.what_is_the_cheapest_route('SNA', 'DCA')
        self.assertEqual(
            res, ([('SNA', 'LAX'), ('LAX', 'DCA')], 1329),
            "They direction is not right")

    def test_CheapestRouteRightCost(self):
        '''bug6 The cheapest route's cost should be the cheapest'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        _, cost = ra.what_is_the_cheapest_route('SNA', 'JFK')
        self.assertEqual(cost, 1643, "the cheapest cost is 1643")

    def test_TerminateFlight(self):
        '''bug 7: test remove related edge when terminate flight '''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)

        start_vertex = None
        end_vertex = None

        for item in ra._airports:
            if item[1] == "SNA":
                start_vertex = ra._flight_map.get_vertex(item[3])
            if item[1] == "LAX":
                end_vertex = ra._flight_map.get_vertex(item[3])
        ra.terminate_flight("SNA", "LAX")
        e = ra._flight_map.get_edge_by_vertexID(
            start_vertex.get_num(), end_vertex.get_num())
        self.assertTrue(e is None, "The edge still exists")


    def test_ShutdownAirportShouldRemoveRelatedFlights(self):
        '''bug8 tests the shutdown_airport should remove related flights'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)

        flights = [flight for flight in ra._flights if flight[
            0] == "SNA" or flight[1] == "SNA"]
        ra.shutdown_airport("SNA")
        count = 0
        for flight in flights:
            if flight in ra._flights:
                count += 1
        self.assertEqual(
            count, 0, "The number of related flights should be zero")

    def test_ShutdownAirportShouldUpdatedFlightMap(self):
        '''bug9 tests the shutdown_airport should update the flight map'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)

        # flight [departureAirportCode, arrivalAirportCode, cost, edge_num]
        # airport [name, code, city, airport_counter, dirty]
        deleted = [flight for flight in ra._flights if flight[
            0] == "SNA" or flight[1] == "SNA"]
        ra.shutdown_airport("SNA")
        edges = [flight[3] for flight in deleted]
        count = 0
        for edge in edges:
            if ra._flight_map.get_edge_by_id(edge) is not None:
                count += 1
        vertex = None
        for item in ra._airports:
            if item[1] == "SNA":
                vertex = ra._flight_map.get_vertex(item[3])
        self.assertEqual(
            count, 0, "the number of related edges should be zero")
        self.assertTrue(
            vertex is None, "The related vertex still exists in flight map")

    def test_Iter(self):
        '''bug 10 test __iter__ should traverse all the flight'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra.add_airport("Los Angeles International Airport",
                       "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.")
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport", "JFK", "New York City")
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)

        flights = list(ra)
        self.assertTrue(len(flights) == 5,
                        "The length of the flights should be 5")

    def test_Equal(self):
        '''Test that __eq__ works correctly'''
        ra1 = RouteAnalyzer()
        ra1.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra1.add_airport("Los Angeles International Airport",
                        "LAX", "Los Angeles")
        ra1.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra1.add_airport("Washington Reagan National Airport",
                        "DCA", "Washington D.C.")
        ra1.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra1.add_airport("Kennedy International Airport",
                        "JFK", "New York City")
        ra1.add_flight('SNA', 'LAX', 230)
        ra1.add_flight('LAX', 'DCA', 1099)
        ra1.add_flight('SDO', 'ORD', 950)
        ra1.add_flight('DCA', 'JFK', 314)
        ra1.add_flight('LAX', 'JFK', 2019)

        ra2 = RouteAnalyzer()
        ra2.add_airport("John Wayne Airport", "SNA", "Santa Ana")
        ra2.add_airport("Los Angeles International Airport",
                        "LAX", "Los Angeles")
        ra2.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra2.add_airport("Washington Reagan National Airport",
                        "DCA", "Washington D.C.")
        ra2.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra2.add_airport("Kennedy International Airport",
                        "JFK", "New York City")
        ra2.add_flight('SNA', 'LAX', 230)
        ra2.add_flight('LAX', 'DCA', 1099)
        ra2.add_flight('SDO', 'ORD', 950)
        ra2.add_flight('DCA', 'JFK', 314)
        ra2.add_flight('LAX', 'JFK', 2019)
        # add a new flight 
        ra2.add_flight("LAX", "ORD", 1200)
        self.assertFalse(ra1==ra2, "ra1 and ra2 should't be equal")

    def test_CheapestRouteWithoutDirtyLayovers(self):
        '''test what_is_the_cheapest_route_with_no_dirty_airport_layovers'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana",True)
        ra.add_airport("Los Angeles International Airport", "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.", True)
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport",
                       "JFK", "New York City", True)
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        # ra.printState()
        res = ra.what_is_the_cheapest_route_with_no_dirty_airport_layovers('SNA', 'JFK')
        self.assertEqual(res, ([('SNA', 'LAX'), ('LAX', 'JFK')], 2249))

    def test_FewestLayoverRoute(self):
        '''test function what_is_the_route_with_the_fewest_layovers'''
        ra = RouteAnalyzer()
        ra.add_airport("John Wayne Airport", "SNA", "Santa Ana",True)
        ra.add_airport("Los Angeles International Airport", "LAX", "Los Angeles")
        ra.add_airport("San Diego International Airport", "SDO", "San Diego")
        ra.add_airport("Washington Reagan National Airport",
                       "DCA", "Washington D.C.", True)
        ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
        ra.add_airport("Kennedy International Airport",
                       "JFK", "New York City", True)
        ra.add_flight('SNA', 'LAX', 230)
        ra.add_flight('LAX', 'DCA', 1099)
        ra.add_flight('SDO', 'ORD', 950)
        ra.add_flight('DCA', 'JFK', 314)
        ra.add_flight('LAX', 'JFK', 2019)
        # ra.printState()
        res = ra.what_is_the_route_with_the_fewest_layovers('SNA', 'JFK')
        self.assertEqual(res, ([('SNA', 'LAX'), ('LAX', 'JFK')], 2249))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
