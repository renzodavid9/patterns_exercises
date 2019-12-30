const ConcreteStrategyA = require('./ConcreteStrategyA.js');
const ConcreteStrategyB = require('./ConcreteStrategyB.js');

class StrategyContext {
  constructor(strategies){
    this.strategies_ = new Map(strategies);
  }

  runStrategy(strategyName) {
    const concreteStrategy = this.strategies_.get(strategyName);
    if (concreteStrategy) {
      concreteStrategy.run();
    } else {
      throw 'Strategy not found';
    }
  }
}

module.exports = new StrategyContext([
    ['A', new ConcreteStrategyA],
    ['B', new ConcreteStrategyB],
]);