const strategyContext =  require('./StrategyContext.js');

class Main {
  constructor(strategyContext) {
    this.strategyContext = strategyContext;
  }

  run() {
    try {
      this.strategyContext.runStrategy('A');
      this.strategyContext.runStrategy('B');
      this.strategyContext.runStrategy('C');
    } catch (error) {
      console.error(error);
    }

  }
}



const main = new Main(strategyContext);
main.run();