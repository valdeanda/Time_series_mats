install.packages("visNetwork")
#devtools::install_github("datastorm-open/visNetwork") #for development version
library(visNetwork)

setwd("D:/2 Escritorio/Networks_figures")



#Read Edges

edgesA<-read.table("edgesA.txt", header=TRUE,sep="\t")
edgesB<-read.table("edgesB.txt", header=TRUE,sep="\t")
edgesC<-read.table("edgesC.txt", header=TRUE,sep="\t")

#Read Nodes 

nodesA<-read.table("nodesA.txt", header = TRUE, sep="\t")
nodesB<-read.table("nodesB.txt", header = TRUE, sep="\t")
nodesC<-read.table("nodesC.txt", header = TRUE, sep="\t")


#to html customizables 
#SITE A 


siteA_network<-visNetwork(nodesA,edgesA, height = "700px", width = "100%",main = "Site A") %>%
  visLegend()%>%
  visEdges(arrows="to")%>%
  visOptions(selectedBy = "group", 
             highlightNearest = TRUE, 
             nodesIdSelection = TRUE,
             manipulation=TRUE) %>%
  visPhysics(enable=TRUE)%>%
  visConfigure(enabled=TRUE)
visSave(siteA_network, file = "networkA.html")

#to html customizables 
#SITE B

siteB_network<-visNetwork(nodesB,edgesB, height = "700px", width = "100%",main = "Site B") %>%
  visLegend()%>%
  visEdges(arrows="to")%>%
  visOptions(selectedBy = "group", 
             highlightNearest = TRUE, 
             nodesIdSelection = TRUE,
             manipulation=TRUE) %>%
  visPhysics(enable=TRUE)%>%
  visConfigure(enabled=TRUE)
siteB_network
visSave(siteB_network, file = "networkB.html")


#to html customizables 
#SITE C

siteC_network<-visNetwork(nodesC,edgesC, height = "700px", width = "100%",main = "Site C") %>%
  visLegend()%>%
  visEdges(arrows="to")%>%
  visOptions(selectedBy = "group", 
             highlightNearest = TRUE, 
             nodesIdSelection = TRUE,
             manipulation=TRUE) %>%
  visPhysics(enable=TRUE)%>%
  visConfigure(enabled=TRUE)
siteC_network
visSave(siteB_network, file = "networkC.html")




