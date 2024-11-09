import unittest
from PyColor.pycolor import Colorate, ColorGradients, Direction, ColorateSystem


class TestTerminalSupport(unittest.TestCase):

    def test_terminal_size(self):
        # Verifica che `get_terminal_size` restituisca un tuple (cols, rows)
        cols, rows = ColorateSystem().get_terminal_size()
        self.assertIsInstance(cols, int)
        self.assertIsInstance(rows, int)
        self.assertGreaterEqual(cols, 0)
        self.assertGreaterEqual(rows, 0)


class TestColorGradients(unittest.TestCase):

    def test_gradient_enums(self):
        # Verifica che le varianti dei gradienti siano stringhe valide ANSI
        for gradient in ColorGradients:
            for color_code in gradient.value:
                self.assertTrue(color_code.startswith("\033[38;2;"), f"{gradient} non è valido")


class TestColorate(unittest.TestCase):

    def setUp(self):
        self.colorate = Colorate()

    def test_reset_constant(self):
        # Verifica che il codice RESET sia un codice ANSI
        self.assertEqual(self.colorate.RESET, "\033[0m")

    def test_gradient_text_horizontal(self):
        # Test di un semplice testo con gradienti orizzontali
        result = self.colorate.gradient_text("Test", ColorGradients.RED_GRADIENTS, direction=Direction.HORIZONTAL)
        self.assertIn("\033[38;2;", result)

    def test_gradient_text_wave(self):
        # Testa il gradiente direzionale a onda per il testo
        result = self.colorate.gradient_text("Test wave", ColorGradients.BLUE_GRADIENTS, direction=Direction.WAVE)
        self.assertIn("\033[38;2;", result)

    def test_gradient_text_invalid_gradient(self):
        # Verifica l’errore per gradienti non validi
        with self.assertRaises(ValueError):
            self.colorate.gradient_text("Test", "non-valid-gradient")

    def test_gradient_text_invalid_direction(self):
        # Verifica che direzioni non valide sollevino un errore
        with self.assertRaises(ValueError):
            self.colorate.gradient_text("Test", ColorGradients.GREEN_GRADIENTS, direction="not-a-direction")


class TestInterpolation(unittest.TestCase):

    def setUp(self):
        self.colorate = Colorate()

    def test_interpolate_colors(self):
        # Test di interpolazione tra due colori RGB
        color1 = [0, 0, 255]  # blu
        color2 = [255, 0, 0]  # rosso
        result = self.colorate._interpolate_colors(color1, color2, 0.5)
        self.assertEqual(result, (127, 0, 127))

    def test_parse_ansi_color(self):
        # Test per estrarre valori RGB da un codice ANSI
        result = self.colorate._parse_ansi_color("\033[38;2;255;100;50m")
        self.assertEqual(result, (255, 100, 50))


if __name__ == "__main__":
    unittest.main()
