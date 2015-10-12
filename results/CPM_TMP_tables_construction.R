source("https://bioconductor.org/biocLite.R")
biocLite("edgeR")

#link to a page with documentations
#http://www.bioconductor.org/packages/release/bioc/html/edgeR.html
library("edgeR")

x <- read.delim("data.txt", sep = " ", header = TRUE, row.names = 1)
d <- DGEList(counts=x)

#two ways of CPM table construction
CPM <- cpm(d)
cpm_test <- apply(x, 2, function(x) (x/sum(x))*1000000) 

library("caroline")
write.delim(CPM, "cpm.txt", row.names = TRUE, sep = " ")

gene_names <- row.names(x)
write.table(gene_names, file = "gene_names.txt", row.names = FALSE, quote = FALSE)

gene_info <- read.delim("mart_export.txt", sep=",", header = TRUE, row.names = 1)
gene_info <- transform(gene_info, length = Gene.End..bp. - Gene.Start..bp.)
gene_info <- gene_info["length"]
x <- merge(x, gene_info, by = 0, all.x = TRUE)
Genes_not_found <- subset(x,  is.na(length))
x <- subset(x,  !is.na(length), drop = TRUE)
rownames(x) <- x[,1]
x[,1] <- NULL

TPM <- lapply(x, function(y) (y/x$length))
TPM <- as.data.frame(TPM)
row.names(TPM) <- row.names(x)
TPM[,84] <-NULL
TPM <- apply(x, 2, function(x) (x/sum(x))*1000000) 
write.delim(TPM, "TPM_without_some_genes.txt", row.names = TRUE, sep = " ")

write.table(Genes_not_found$Row.names, file = "gene_not_found_names.txt", row.names = FALSE, quote = FALSE)


