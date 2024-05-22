import joblib
from pgmpy.inference import VariableElimination

model=joblib.load('G:\OneDrive - northsouth.edu\CODES\PROJECTS\PROJECT-MYSTERY SOLVER\Bayesian_model.joblib')

class BayesianModel:

    def solve_mystery(evidence,query_vars):
        if model is None:
            return False
        inference=VariableElimination(model=model)
        try:
            results = inference.query(variables=query_vars, evidence=evidence, joint=False)
            formatted_results = {}
            for var in query_vars:
                factor = results[var]
                states = factor.state_names[var]
                probabilities = factor.values
                formatted_results[var] = {state: round(prob, 3) for state, prob in zip(states, probabilities)}
            return formatted_results
        except Exception as e:
            print(f"Error during inference: {e}")
            return {}
