/*
 * This file contains helper functions to deal with command line options.
 */

/*
 * This function handles command line optoins, it uses the Boost library to
 * parse the command line options.
 * The options are:
 *   * -h, --help: print help message
 *   * -N, --number: number of iterations
 *   * -n, --number of particles
 *   * -T, --temperature
 *   * -s, --seed
 * It returns the resulting options as a tuple.  
 */
auto parse_command_line_args(int argc, char **argv) {
  namespace po = boost::program_options;
  po::options_description desc("Allowed options");
  desc.add_options()("help,h", "produce help message")(
      "number,N", po::value<int>()->default_value(1000), "number of iterations")(
      "particles,n", po::value<int>()->default_value(1000),
      "number of particles")("temperature,T", po::value<double>()->default_value(1.0),
      "temperature")("seed,s", po::value<int>()->default_value(0), "seed");
  po::variables_map vm;
  po::store(po::parse_command_line(argc, argv, desc), vm);
  if (vm.count("help")) {
    std::cout << desc;
    exit(0);
  }
  po::notify(vm);
  return std::make_tuple(vm["number"].as<int>(), vm["particles"].as<int>(),
                         vm["temperature"].as<double>(), vm["seed"].as<int>());
}
