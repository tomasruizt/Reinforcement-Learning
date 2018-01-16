import unittest

from Setting10x10.TenTimesTenAgent import TenTimesTenAgent


class TenTimesTenAgentTest(unittest.TestCase):
    def setUp(self):
        self.action = "action"
        self.estimate = 1.0
        self.state_new = (1, 1)
        self.actions_available_new = ["actions_available_new"]
        self.reward = 100.0

    def test_observe(self):
        agent = TenTimesTenAgent()
        agent.observe(self.state_new, self.actions_available_new, self.reward)
        history = agent.get_history()
        reward, state = history[-1][:2]

        self.assertEqual(state, self.state_new)
        self.assertEqual(reward, self.reward)

    def test_game_finished(self):
        agent = TenTimesTenAgent()
        agent._log_action(self.action, self.estimate)
        agent.game_finished()
        history = agent.get_history()
        history_new = TenTimesTenAgent().get_history()

        self.assertEqual(history, history_new)

    def test_get_states_neighboring(self):
        agent = TenTimesTenAgent()
        agent.observe((9, 0), ["up", "left"], 0)
        states = agent._get_states_neighboring()
        self.assertIn((9, 1), states)
        self.assertIn((8, 0), states)

        agent.observe((0, 9), ["down", "right"], 0)
        states = agent._get_states_neighboring()
        self.assertIn((1, 9), states)
        self.assertIn((0, 8), states)

    def test_log_action(self):
        agent = TenTimesTenAgent()
        agent._log_action(self.action, self.estimate)
        history = agent.get_history()

        action, estimate = history[-1][2:]
        self.assertEqual(action, self.action)
        self.assertEqual(estimate, self.estimate)

    def test_take_action(self):
        with self.assertRaises(NotImplementedError):
            TenTimesTenAgent().take_action()


