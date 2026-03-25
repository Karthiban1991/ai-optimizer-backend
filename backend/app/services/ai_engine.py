class AIEngine:

    def optimize(self, pods):
        actions = []

        for p in pods:
            actions.append({
                "pod": p["name"],
                "action": "scale_down"
            })

        return actions
