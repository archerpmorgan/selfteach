export function bookSummaryStatistics(book) {
    let totalProblems = 0;
    let completedProblems = 0;
    book.sections.forEach((section) => {
      section.problems.forEach((problem) => {
        totalProblems++;
        if (problem.completed) {
          completedProblems++;
        }
      });
    });
  
    let totalSections = 0;
    let studiedSections = 0;
    book.sections.forEach((section) => {
      totalSections++;
      if (section.haveStudied) {
        studiedSections++;
      }
    });
  
    return {
      totalProblems,
      completedProblems,
      totalSections,
      studiedSections,
    };
  }