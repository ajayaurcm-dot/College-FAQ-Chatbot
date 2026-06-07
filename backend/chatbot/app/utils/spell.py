import os
from symspellpy import SymSpell, Verbosity


class SpellCorrector:
    def __init__(self):
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

        # Load dictionary
        dictionary_path = os.path.join(
            os.path.dirname(__file__),
            "frequency_dictionary_en_82_765.txt"
        )

        if not os.path.exists(dictionary_path):
            print("[SPELL ERROR] Dictionary file not found")
        else:
            self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    # ---------------------------
    # Correct sentence
    # ---------------------------
    def correct(self, text: str) -> str:
        try:
            suggestions = self.sym_spell.lookup_compound(
                text,
                max_edit_distance=2
            )

            return suggestions[0].term if suggestions else text

        except Exception as e:
            print(f"[SPELL ERROR] {e}")
            return text