from utils.parameter import Parameter


class RuleHandler:
    def __init__(self):
        # We're going to parse rules string take from the settings file into a list of rules
        self.rules: list[tuple[int, str]] = []

        for rule in Parameter.rules.split(","):
            # Split the rule into a tuple (state, result)
            state, result = rule.split(":")
            self.rules.append((int(state), result))

    def apply_rules(self, state: int, neighbours_number: int) -> int:
        """
            Check if there's a matching between the current state and the neighbours' number
            :param state: the state of the current tile
            :param neighbours_number: the number of neighbours of the current tile
            :return: next state of the current tile
        """

        for rule in self.rules:
            if rule[0] == state:

                if "-" in rule[1]:  # Neighbours number is within the range specified
                    start, end = rule[1].split("-")  # x-y
                    if int(start) <= neighbours_number <= int(end):
                        return 1

                elif "<" in rule[1]:  # Neighbours number is less than specified
                    end = rule[1][1:]  # <y
                    if neighbours_number < int(end):
                        return 1

                elif ">" in rule[1]:  # Neighbours number is greater than specified
                    start = rule[1][1:]  # >x
                    if int(start) < neighbours_number:
                        return 1

                else:  # Neighbours number exactly matching with specified x
                    if neighbours_number == int(rule[1]):
                        return 1

        return 0
