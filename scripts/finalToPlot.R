install.packages("visNetwork")
#devtools::install_github("datastorm-open/visNetwork") #for development version
library(visNetwork)

#Read Edges

edgesA<-read.table("../data/edgesA.txt", header=TRUE,sep="\t")
edgesB<-read.table("../data/edgesB.txt", header=TRUE,sep="\t")
edgesC<-read.table("../data/edgesC.txt", header=TRUE,sep="\t")

#Read Nodes 

nodesA<-read.table("../data/nodesA.txt", header = TRUE, sep="\t")
nodesB<-read.table("../data/nodesB.txt", header = TRUE, sep="\t")
nodesC<-read.table("../data/nodesC.txt", header = TRUE, sep="\t")


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

