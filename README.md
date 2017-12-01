# PageRank
PageRank (PR) is an algorithm used by Google Search to rank websites in their search engine results. PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites. <a href = "https://en.wikipedia.org/wiki/PageRank"> Wiki </a>

As part of Information Retrievel course assignment, implemented PageRank algorithm.

# Input Format
The the python file accepts any kind of text file of Adjacency matrix with three columns of (i, j, k) where each row will denote information for a cell. A row of the form "i j k" denotes that the matrix contains a value k at the row i column j. Run the file python <a href = "https://github.com/ginugat/PageRank/blob/master/PageRankImplementation.py"> pageRankImplementation.py </a> and as prompted, give the path of the Adjacency Matrix of above format as input.

The Algorithm outputs:
  
  1) Stochastic matrix M: 
  
  2) Original rank vector rj: 
  
  3) Converged rank vector (R):
  
  4) Number of iterations took to converge: 


# Matrix formulation for random surfer model
v' = &beta;Mv + (1-&beta;)e/N

Assumptions: 

Damping Factor &beta; = 0.85

Threshold value to check the convergence condition &epsilon; = 0.0001


