function generateActionQueue() {

  const duplicateGroups = detectDuplicateGroups();

  const engine = new RecommendationEngine();

  const recommendations =
    engine.generate(duplicateGroups);

  const queue = new ActionQueue();

  queue.write(recommendations);

}