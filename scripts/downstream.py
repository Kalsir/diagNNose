from diagnnose.config.arg_parser import create_arg_parser
from diagnnose.config.setup import ConfigSetup
from diagnnose.models.import_model import import_model_from_json
from diagnnose.models.language_model import LanguageModel
from diagnnose.downstream.suite import DownstreamSuite


if __name__ == "__main__":
    arg_groups = {"model", "vocab", "downstream"}
    arg_parser, required_args = create_arg_parser(arg_groups)

    config_dict = ConfigSetup(arg_parser, required_args, arg_groups).config_dict

    model: LanguageModel = import_model_from_json(config_dict["model"])

    suite = DownstreamSuite(
        device=config_dict["model"].get("device", "cpu"), **config_dict["downstream"]
    )

    results = suite.perform_tasks(model, config_dict["vocab"]["vocab_path"])
