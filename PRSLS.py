import random, math
from collections import Counter, deque

#REGRAS
MOVES = ["pedra", "papel", "tesoura", "lagarto", "spock"]

RULES = {
    "pedra": {"vence": ["tesoura", "lagarto"], "perde": ["papel", "spock"]},
    "papel": {"vence": ["pedra", "spock"], "perde": ["tesoura", "lagarto"]},
    "tesoura": {"vence": ["papel", "lagarto"], "perde": ["pedra", "spock"]},
    "lagarto": {"vence": ["papel", "spock"], "perde": ["pedra", "tesoura"]},
    "spock": {"vence": ["pedra", "tesoura"], "perde": ["papel", "lagarto"]}
}

VICTORY_MESSAGES = {
    ("pedra", "tesoura"): "Pedra esmaga Tesoura",
    ("pedra", "lagarto"): "Pedra esmaga Lagarto",
    ("papel", "pedra"): "Papel cobre Pedra",
    ("papel", "spock"): "Papel refuta Spock",
    ("tesoura", "papel"): "Tesoura corta Papel",
    ("tesoura", "lagarto"): "Tesoura decapita Lagarto",
    ("lagarto", "papel"): "Lagarto come Papel",
    ("lagarto", "spock"): "Lagarto envenena Spock",
    ("spock", "pedra"): "Spock vaporiza Pedra",
    ("spock", "tesoura"): "Spock quebra Tesoura"
}


def quem_vence(j1, j2):
    #Determina vencedor e mensagem
    if j1 == j2:
        return "empate", "Empate!"

    if j2 in RULES[j1]["vence"]:
        msg = VICTORY_MESSAGES.get((j1, j2), f"{j1} vence {j2}")
        return "j1", msg
    else:
        msg = VICTORY_MESSAGES.get((j2, j1), f"{j2} vence {j1}")
        return "j2", msg


#DIFICULDADE
class DifficultyConfig:
    """Configurações que variam por dificuldade"""

    EASY = {
        "name": "Fácil",
        "icon": ":)",
        "description": "IA previsível, comete erros frequentes",
        "fuzzy_weight": 0.3,
        "dfs_weight": 0.4,
        "nn_weight": 0.3,
        "random_factor": 0.5,
        "learning_rate": 0.05,
        "ga_population": 4,
        "ga_mutation_rate": 0.1,
        "use_pattern_memory": False,
        "strategic_error_chance": 0.30  # 30% de erro proposital
    }

    MEDIUM = {
        "name": "Médio",
        "icon": ":|",
        "description": "IA equilibrada, aprende aos poucos",
        "fuzzy_weight": 0.6,
        "dfs_weight": 0.7,
        "nn_weight": 0.7,
        "random_factor": 0.3,
        "learning_rate": 0.15,
        "ga_population": 6,
        "ga_mutation_rate": 0.2,
        "use_pattern_memory": True,
        "strategic_error_chance": 0.15
    }

    HARD = {
        "name": "Difícil",
        "icon": ":<",
        "description": "IA agressiva, aprende rapidamente",
        "fuzzy_weight": 1.0,
        "dfs_weight": 1.2,
        "nn_weight": 1.0,
        "random_factor": 0.15,
        "learning_rate": 0.20,
        "ga_population": 8,
        "ga_mutation_rate": 0.25,
        "use_pattern_memory": True,
        "strategic_error_chance": 0.08
    }

    EXTREME = {
        "name": "Extremo",
        "icon": ">:(",
        "description": "IA implacável, prediz seus movimentos",
        "fuzzy_weight": 1.5,
        "dfs_weight": 1.8,
        "nn_weight": 1.5,
        "random_factor": 0.05,
        "learning_rate": 0.25,
        "ga_population": 10,
        "ga_mutation_rate": 0.30,
        "use_pattern_memory": True,
        "strategic_error_chance": 0.02
    }

    @staticmethod
    def get_config(difficulty):
        configs = {
            1: DifficultyConfig.EASY,
            2: DifficultyConfig.MEDIUM,
            3: DifficultyConfig.HARD,
            4: DifficultyConfig.EXTREME
        }
        return configs.get(difficulty, DifficultyConfig.MEDIUM)


#FUZZY
def fuzzy_membership(value, low, medium, high):
    #Calcula grau de pertinência fuzzy
    memberships = {}

    if value <= low:
        memberships['baixo'] = 1.0
    elif value <= medium:
        memberships['baixo'] = (medium - value) / (medium - low)
    else:
        memberships['baixo'] = 0.0

    if value <= low:
        memberships['medio'] = 0.0
    elif value <= medium:
        memberships['medio'] = (value - low) / (medium - low)
    elif value <= high:
        memberships['medio'] = (high - value) / (high - medium)
    else:
        memberships['medio'] = 0.0

    if value <= medium:
        memberships['alto'] = 0.0
    elif value <= high:
        memberships['alto'] = (value -   medium) / (high - medium)
    else:
        memberships['alto'] = 1.0

    return memberships


def fuzzy_inference(history, difficulty_config):
    #Sistema de inferência fuzzy
    if len(history) < 4:
        return {"estilo": "equilibrado", "graus": {}, "preferencias": {}}

    #Janela adaptativa baseada na dificuldade
    window = min(len(history), 15 if difficulty_config['use_pattern_memory'] else 8)
    recent_history = history[-window:]

    cont = Counter(recent_history)
    total = len(recent_history)

    frequencias = {move: cont[move] / total for move in MOVES}

    fuzzy_scores = {}
    for move in MOVES:
        fuzzy_scores[move] = fuzzy_membership(frequencias[move], 0.12, 0.20, 0.35)

    estilos = {
        "agressivo_fisico": (fuzzy_scores["pedra"]['alto'] + fuzzy_scores["tesoura"]['alto']) / 2,
        "estrategista": (fuzzy_scores["spock"]['alto'] + fuzzy_scores["papel"]['alto']) / 2,
        "imprevisivel": fuzzy_scores["lagarto"]['alto'],
        "classico": (fuzzy_scores["pedra"]['medio'] + fuzzy_scores["papel"]['medio'] + fuzzy_scores["tesoura"]['medio']) / 3,
        "equilibrado": min(fuzzy_scores[m]['medio'] for m in MOVES)
    }

    if len(set(history[-5:])) >= 4:
        estilos["imprevisivel"] += 0.3

    estilo = max(estilos.items(), key=lambda x: x[1])[0]

    return {
        "estilo": estilo,
        "graus": estilos,
        "preferencias": frequencias
    }


# DFS

def dfs_analyze_sequences(history, difficulty_config):
    #DFS adaptado à dificuldade
    if len(history) < 3:
        return None

    # Profundidade varia com dificuldade
    depth = 2 if not difficulty_config['use_pattern_memory'] else 3

    sequence_patterns = {}

    def dfs_explore(current_seq, nivel, start_pos):
        if nivel == 0:
            return

        for i in range(start_pos, len(history)):
            new_seq = current_seq + [history[i]]
            seq_key = tuple(new_seq)

            count = 0
            for j in range(len(history) - len(new_seq) + 1):
                if history[j:j + len(new_seq)] == new_seq:
                    count += 1

            if count > 0:
                sequence_patterns[seq_key] = count
                dfs_explore(new_seq, nivel - 1, i + 1)

    dfs_explore([], depth, 0)

    # Análise de transições
    transitions = {}
    window = min(len(history), 20)
    for i in range(len(history) - window, len(history) - 1):
        if i >= 0:
            key = (history[i], history[i + 1])
            transitions[key] = transitions.get(key, 0) + 1

    if history:
        last = history[-1]
        possible_next = [(move, transitions.get((last, move), 0))
                        for move in MOVES]
        predicted = max(possible_next, key=lambda x: x[1])[0]

        if transitions.get((last, predicted), 0) == 0:
            predicted = max(Counter(history[-10:]).items(), key=lambda x: x[1])[0]

        return predicted

    return random.choice(MOVES)


# REDE NEURAL SIMPLIFICADA
class SimpleNeuralNet:
    def __init__(self, difficulty_config):
        self.input_size = 15
        self.output_size = 5
        self.hidden_size = 10 if difficulty_config['use_pattern_memory'] else 6

        self.weights_hidden = [[random.uniform(-0.5, 0.5) for _ in range(self.input_size)]
                               for _ in range(self.hidden_size)]
        self.weights_output = [[random.uniform(-0.5, 0.5) for _ in range(self.hidden_size)]
                               for _ in range(self.output_size)]

        self.learning_rate = difficulty_config['learning_rate']
        self.momentum = 0.05
        self.prev_delta_hidden = [[0] * self.input_size for _ in range(self.hidden_size)]
        self.prev_delta_output = [[0] * self.hidden_size for _ in range(self.output_size)]

    def encode_move(self, move): #CONVERTE EM ONE-HOT-ENCONDING
        encoding = {m: [0] * 5 for m in MOVES}
        for i, m in enumerate(MOVES):
            encoding[m][i] = 1
        return encoding[move]

    def decode_output(self, output): #GERA 5 PROBABILIDADES
        max_idx = output.index(max(output))
        return MOVES[max_idx]

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-max(-500, min(500, x))))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs): #MULTIPLICA ENTRADAS
        hidden = []
        for neuron_weights in self.weights_hidden:
            activation = sum(w * i for w, i in zip(neuron_weights, inputs))
            hidden.append(self.sigmoid(activation))

        outputs = []
        for neuron_weights in self.weights_output:
            activation = sum(w * h for w, h in zip(neuron_weights, hidden))
            outputs.append(self.sigmoid(activation))

        return hidden, outputs

    def predict(self, history): #PEGA AS 3 ULTIMAS JOGADAS
        if len(history) < 3:
            return random.choice(MOVES)

        inputs = []
        for move in history[-3:]:
            inputs.extend(self.encode_move(move))

        _, outputs = self.forward(inputs)
        return self.decode_output(outputs)

    def train(self, history, actual_move):
        if len(history) < 3:
            return

        inputs = []
        for move in history[-3:]:
            inputs.extend(self.encode_move(move))

        hidden, outputs = self.forward(inputs)

        target = self.encode_move(actual_move)
        output_errors = [t - o for t, o in zip(target, outputs)]
        output_deltas = [e * self.sigmoid_derivative(o)
                        for e, o in zip(output_errors, outputs)]

        hidden_errors = [0] * len(hidden)
        for i in range(len(hidden)):
            error = sum(output_deltas[j] * self.weights_output[j][i]
                       for j in range(self.output_size))
            hidden_errors[i] = error

        hidden_deltas = [e * self.sigmoid_derivative(h)
                        for e, h in zip(hidden_errors, hidden)]

        for i in range(self.output_size):
            for j in range(len(hidden)):
                delta = self.learning_rate * output_deltas[i] * hidden[j]
                delta += self.momentum * self.prev_delta_output[i][j]
                self.weights_output[i][j] += delta
                self.prev_delta_output[i][j] = delta

        for i in range(len(hidden)):
            for j in range(len(inputs)):
                delta = self.learning_rate * hidden_deltas[i] * inputs[j]
                delta += self.momentum * self.prev_delta_hidden[i][j]
                self.weights_hidden[i][j] += delta
                self.prev_delta_hidden[i][j] = delta


# A*

class AStarDecision:
    def __init__(self, difficulty_config):
        self.config = difficulty_config
        self.move_costs = {move: 1.0 for move in MOVES}

    def heuristic(self, move, predicted_dfs, nn_prediction, fuzzy_analysis):
        score = 0

        # Pesos ajustados pela dificuldade
        if predicted_dfs in RULES[move]["vence"]:
            score += 12 * self.config['dfs_weight']
        elif predicted_dfs in RULES[move]["perde"]:
            score -= 5 * self.config['dfs_weight']

        if nn_prediction in RULES[move]["vence"]:
            score += 10 * self.config['nn_weight']
        elif nn_prediction in RULES[move]["perde"]:
            score -= 4 * self.config['nn_weight']

        estilo = fuzzy_analysis['estilo']
        preferencias = fuzzy_analysis['preferencias']

        for preferred_move, freq in preferencias.items():
            if freq > 0.25 and preferred_move in RULES[move]["vence"]:
                score += 7 * freq * self.config['fuzzy_weight']

        style_bonus = {
            "agressivo_fisico": {"pedra": 2, "tesoura": 2, "papel": 1, "lagarto": 1, "spock": 0},
            "estrategista": {"spock": 3, "papel": 2, "lagarto": 1, "pedra": 0, "tesoura": 1},
            "imprevisivel": {"lagarto": 3, "spock": 2, "tesoura": 1, "papel": 1, "pedra": 1},
            "classico": {"pedra": 1, "papel": 1, "tesoura": 1, "lagarto": 0, "spock": 0},
            "equilibrado": {m: 1 for m in MOVES}
        }
        score += style_bonus.get(estilo, {}).get(move, 0) * self.config['fuzzy_weight']

        score += random.uniform(0, 2 * self.config['random_factor'])

        return score

    def search_best_move(self, predicted_dfs, nn_prediction, fuzzy_analysis, ia_history):
        candidates = []

        for move in MOVES:
            g_cost = self.move_costs[move]

            if ia_history and move == ia_history[-1]:
                g_cost += 0.5

            if ia_history:
                freq = ia_history.count(move) / len(ia_history)
                if freq > 0.3:
                    g_cost += 1.0

            h_cost = self.heuristic(move, predicted_dfs, nn_prediction, fuzzy_analysis)
            f_cost = -g_cost + h_cost

            candidates.append((move, f_cost))

        best = max(candidates, key=lambda x: x[1])
        return best[0]


# ALGORITMO GENÉTICO
class GeneticAlgorithm:
    def __init__(self, difficulty_config):
        self.config = difficulty_config
        pop_size = difficulty_config['ga_population']

        self.population = [[random.uniform(0.5, 3.0) for _ in range(5)]
                          for _ in range(pop_size)]
        self.fitness_scores = [1.0] * pop_size
        self.generation = 0
        self.best_ever = None
        self.best_fitness = 0

    def evaluate_fitness(self, chromosome, won, rounds_played):
        base = sum(chromosome) / len(chromosome)

        if won:
            fitness = base * 3.0
        else:
            fitness = base * 0.8

        if rounds_played > 10:
            fitness *= 1.2

        return fitness

    def selection(self):
        tournament_size = min(4, len(self.population))
        tournament = random.sample(list(enumerate(self.population)), tournament_size)
        best = max(tournament, key=lambda x: self.fitness_scores[x[0]])
        return best[1]

    def crossover(self, parent1, parent2):
        child = []
        for i in range(len(parent1)):
            child.append(parent1[i] if random.random() < 0.5 else parent2[i])
        return child

    def mutation(self, chromosome):
        rate = self.config['ga_mutation_rate']
        mutated = chromosome[:]
        for i in range(len(mutated)):
            if random.random() < rate:
                mutated[i] += random.gauss(0, 0.4)
                mutated[i] = max(0.2, min(4.0, mutated[i]))
        return mutated

    def evolve(self, best_idx, won, rounds_played):
        fitness = self.evaluate_fitness(self.population[best_idx], won, rounds_played)
        self.fitness_scores[best_idx] = fitness

        if fitness > self.best_fitness:
            self.best_fitness = fitness
            self.best_ever = self.population[best_idx][:]

        self.generation += 1
        evolve_interval = 5 if len(self.population) <= 4 else 4

        if self.generation % evolve_interval == 0:
            new_population = []

            sorted_pop = sorted(enumerate(self.fitness_scores),
                              key=lambda x: x[1], reverse=True)

            elite_count = min(2, len(self.population) // 2)
            for i in range(elite_count):
                new_population.append(self.population[sorted_pop[i][0]])

            if self.best_ever and len(new_population) < len(self.population):
                new_population.append(self.best_ever)

            while len(new_population) < len(self.population):
                p1 = self.selection()
                p2 = self.selection()
                child = self.crossover(p1, p2)
                child = self.mutation(child)
                new_population.append(child)

            self.population = new_population
            self.fitness_scores = [1.0] * len(self.population)

    def get_best_weights(self):
        best_idx = max(enumerate(self.fitness_scores), key=lambda x: x[1])[0]
        return self.population[best_idx], best_idx

# SISTEMA DE JOGO COM DIFICULDADES
def select_difficulty():
    #Menu de seleção de dificuldade
    print("\n" + "="*70)
    print(" SELECIONE A DIFICULDADE:")
    print("="*70)

    difficulties = [
        (1, DifficultyConfig.EASY),
        (2, DifficultyConfig.MEDIUM),
        (3, DifficultyConfig.HARD),
        (4, DifficultyConfig.EXTREME)
    ]

    for num, config in difficulties:
        print(f"  [{num}] {config['icon']} {config['name'].upper()}")
        print(f"      {config['description']}")

    print("="*70)

    while True:
        try:
            choice = input("\n  Escolha (1-4): ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= 4:
                return choice_num
            print(" Escolha um número entre 1 e 4!")
        except ValueError:
            print(" Digite um número válido!")


def play_game():
    #Seleção de dificuldade
    difficulty_level = select_difficulty()
    config = DifficultyConfig.get_config(difficulty_level)

    #Inicializa sistemas de IA com configurações
    neural_net = SimpleNeuralNet(config)
    a_star = AStarDecision(config)
    genetic = GeneticAlgorithm(config)

    player_history = []
    ia_history = []
    stats = {"ia": 0, "player": 0, "empate": 0}

    print("\n" + "="*70)
    print(f" MODO: {config['icon']} {config['name'].upper()}")
    print(" PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK COM IA AVANÇADA")
    print("="*70)
    print("\n REGRAS:")
    print(" Pedra esmaga Tesoura e Lagarto")
    print(" Papel cobre Pedra e refuta Spock")
    print(" Tesoura corta Papel e decapita Lagarto")
    print(" Lagarto come Papel e envenena Spock")
    print(" Spock vaporiza Pedra e quebra Tesoura")
    print("="*70 + "\n")

    round_num = 0

    while True:
        round_num += 1
        print(f"\n{'─'*70}")
        jogada = input(f"[Rodada {round_num}] Jogada (pedra/papel/tesoura/lagarto/spock ou 'sair'): ").lower().strip()

        if jogada == "sair":
            print("\n" + "="*70)
            print(f" RESULTADO FINAL - {config['icon']} {config['name'].upper()}:")
            print(f" IA: {stats['ia']} vitórias")
            print(f" Você: {stats['player']} vitórias")
            print(f" Empates: {stats['empate']}")
            total_jogos = stats['ia'] + stats['player']
            if total_jogos > 0:
                taxa_ia = stats['ia'] / total_jogos * 100
                taxa_player = stats['player'] / total_jogos * 100
                print(f" Taxa de vitória da IA: {taxa_ia:.1f}%")
                print(f" Sua taxa de vitória: {taxa_player:.1f}%")
            print(f" Gerações evoluídas: {genetic.generation}")
            print("="*70)
            break

        if jogada not in MOVES:
            print("! Jogada inválida! Use: pedra, papel, tesoura, lagarto ou spock")
            continue

        player_history.append(jogada)

        #ANÁLISE DA IA
        fuzzy_result = fuzzy_inference(player_history, config)
        predicted_dfs = dfs_analyze_sequences(player_history, config)
        if not predicted_dfs:
            predicted_dfs = random.choice(MOVES)

        nn_prediction = neural_net.predict(player_history)

        #DECISÃO FINAL COM POSSÍVEL ERRO ESTRATÉGICO
        ia_move_optimal = a_star.search_best_move(
            predicted_dfs,
            nn_prediction,
            fuzzy_result,
            ia_history
        )

        #Erro estratégico baseado na dificuldade
        if random.random() < config['strategic_error_chance']:
            #IA "erra" e joga algo aleatório
            ia_move = random.choice(MOVES)
        else:
            ia_move = ia_move_optimal

        ia_history.append(ia_move)

        #RESULTADO
        resultado, mensagem = quem_vence(ia_move, jogada)

        print(f"\n IA jogou: {ia_move.upper()}")
        print(f" Você jogou: {jogada.upper()}")

        if resultado == "empate":
            print(f" {mensagem}")
            stats["empate"] += 1
            won = False
        elif resultado == "j1":
            print(f" IA VENCEU! {mensagem}")
            stats["ia"] += 1
            won = True
        else:
            print(f" VOCÊ VENCEU! {mensagem}")
            stats["player"] += 1
            won = False

        #APRENDIZADO
        if len(player_history) >= 3:
            neural_net.train(player_history[:-1], jogada)

        weights, best_idx = genetic.get_best_weights()
        genetic.evolve(best_idx, won, round_num)

        #Info a cada 5 rodadas
        if round_num % 5 == 0:
            print(f"\n ANÁLISE DA IA:")
            print(f" Dificuldade: {config['icon']} {config['name']}")
            print(f" Estilo detectado: {fuzzy_result['estilo']}")
            print(f" Previsão DFS: {predicted_dfs}")
            print(f" Previsão RNA: {nn_prediction}")
            print(f" Geração GA: {genetic.generation}")
            print(f" Placar: IA {stats['ia']} × {stats['player']} Você")


if __name__ == "__main__":
    play_game()