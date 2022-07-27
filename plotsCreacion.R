
- [ ]  Histplot de comentarios
- [ ]  Piecharts de tipos de servicios

library(ggplot2)
library(paletteer)
library(dplyr)

hoteles <- read.csv("./data2/hoteles_compartidos.csv", stringsAsFactors = TRUE)

#### Modelos de regresión ####

mod_pos_bk <- modelo <- lm(rank_bk~comments_bk+stars_bk+rating_bk, ,data=hoteles)
mod_pos_bk
summary(mod_pos_bk)
pos_bk <- predict.lm(object = mod_pos_bk, 
                     newdata = hoteles[,c("comments_bk","stars_bk","rating_bk")]
)

mod_pos_ta <- modelo <- lm(rank_ta~comments_ta+stars_ta+rating_ta, ,data=hoteles)
mod_pos_ta
summary(mod_pos_ta)
pos_ta <- predict.lm(object = mod_pos_ta, 
                     newdata = hoteles[,c("comments_ta","stars_ta","rating_ta")]
)

###Comparacion
ggplot(data=hoteles, mapping = aes(rank_bk,rank_ta))+geom_point()+
  geom_point(mapping = aes(pos_bk,pos_ta, color="blue"))

### PLOTS ####

#Scatterplot entre los rankings
ggplot(data=hoteles, mapping = aes(rank_bk,rank_ta)) +
  geom_point(color="deepskyblue4") + 
  stat_smooth(method="lm",color="skyblue4", fill="skyblue3") +
  labs(x="Posición en Booking", y="Posición en TripAdvisor",
       title="Comparación de posiciones entre\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,150,15)) +
  scale_y_continuous(breaks = seq(0,300,20)) +
  theme(plot.title = element_text(hjust = 0.5))

# - [ ]  Scatterplot entre los rankings con la info de las estrellas
ggplot(data=hoteles, mapping = aes(rank_bk,rank_ta,size=stars_bk)) +
  geom_point(color="deepskyblue4") + 
  scale_size_continuous(name = "Estrellas", range=c(0,8) ) +
  labs(x="Posición en Booking", y="Posición en TripAdvisor",
       title="Comparación de posiciones entre\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,150,15)) +
  scale_y_continuous(breaks = seq(0,300,20)) +
  theme(plot.title = element_text(hjust = 0.5))

# - [ ]  Scatterplot entre los rankings con la info del precio
ggplot(data=hoteles, mapping = aes(rank_bk,rank_ta,color=prices_bk)) +
  geom_point() + 
  scale_color_paletteer_c("ggthemes::Classic Blue",direction=1)+
  labs(x="Posición en Booking", y="Posición en TripAdvisor",
       color="Precio por noche\n(MXN)",
       title="Comparación de posiciones entre\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,150,15)) +
  scale_y_continuous(breaks = seq(0,300,20)) +
  theme(plot.title = element_text(hjust = 0.5))


#- [ ]  Scatterplot general entre los rankings con la info de los PM
ggplot(data=hoteles, mapping = aes(rank_bk,rank_ta, color=city_ta, shape=city_ta)) +
  geom_point(size=3.5) + 
  scale_colour_paletteer_d("ggthemes::excel_Blue_II") +
  labs(x="Posición en Booking", y="Posición en TripAdvisor",
       color="Pueblo Mágico", shape="Pueblo Mágico",
       title="Comparación de posiciones entre\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,150,15)) +
  scale_y_continuous(breaks = seq(0,300,20)) +
  theme(plot.title = element_text(hjust = 0.5))
  
#- [ ]  Scatterplot comparando la cantidad de comentarios

ggplot(data=hoteles, mapping = aes(comments_bk,comments_ta)) +
  geom_point(color="deepskyblue4") + 
  geom_text(aes(comments_bk,comments_ta,label = name), hjust=-.03,
            data = hoteles[hoteles$comments_ta>1000,], size=3)+
  labs(x="Comentarios en Booking", y="Comentarios en TripAdvisor",
       title="Comparación de comentarios entre\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,1000,100)) +
  scale_y_continuous(breaks = seq(0,5550,250)) +
  theme(plot.title = element_text(hjust = 0.5))

#- [ ]  Scatterplot comparando los servicios presentados
ggplot(data=hoteles) +
  geom_point(aes(x=total_heredados_bk, total_heredados_ta, color="Heredados")) + 
  geom_point(aes(x=total_acceso.comunicacion_bk, total_acceso.comunicacion_ta, color="Comunicación"),shape=15)+
  geom_point(aes(x=total_entretenimiento.deporte_bk, total_entretenimiento.deporte_ta, color="Entretenimiento"),shape=8)+
  geom_point(aes(x=total_ninios_bk, total_ninios_ta, color="Niños"),shape=13)+
  geom_point(aes(x=total_comida.bebida_bk, total_comida.bebida_ta, color="Comida"),shape=14)+

  labs(x="Registrados en Booking", y="Registrados en TripAdvisor",
       color="Tipo de Servicio", shape="Tipo de Servicio",
       title="Comparación de servicios registrados en\nBooking y TripAdvisor") +
  scale_x_continuous(breaks = seq(0,36,3)) +
  scale_y_continuous(breaks = seq(0,10,1)) +
  theme(plot.title = element_text(hjust = 0.5))

#- [ ]  Scatterplot comparando precio vs ranking
ggplot(data=hoteles, mapping = aes(x=prices_bk,y=rank_bk)) +
  geom_point(color="deepskyblue4") + 
  stat_smooth(method="lm",color="skyblue4", fill="skyblue3") +
  labs(x="Precio por noche (MXN)", y="Posición",
       title="Comparación entre precio y posición en\nBooking") +
  scale_x_continuous(breaks = seq(0,11000,500)) +
  scale_y_continuous(breaks = seq(0,300,15)) +
  theme(plot.title = element_text(hjust = 0.5))

ggplot(data=hoteles, mapping = aes(x=prices_ta,y=rank_ta)) +
  geom_point(color="deepskyblue4") + 
  stat_smooth(method="lm",color="skyblue4", fill="skyblue3") +
  labs(x="Precio por noche (MXN)", y="Posición",
       title="Comparación entre precio y posición en\nTripAdvisor") +
  scale_x_continuous(breaks = seq(0,15000,500)) +
  scale_y_continuous(breaks = seq(-200,300,20)) +
  theme(plot.title = element_text(hjust = 0.5))

#- [ ]  Scatterplot comparando precio vs rating
ggplot(data=hoteles, mapping = aes(x=prices_bk,y=rating_bk)) +
  geom_point(color="deepskyblue4") + 
  stat_smooth(method="lm",color="skyblue4", fill="skyblue3") +
  labs(x="Precio por noche (MXN)", y="Evaluación de usario",
       title="Comparación entre precio y evaluación de usuario en\nBooking") +
  scale_x_continuous(breaks = seq(0,11000,500)) +
  scale_y_continuous(breaks = seq(0,10,1)) +
  theme(plot.title = element_text(hjust = 0.5))

ggplot(data=hoteles, mapping = aes(x=prices_ta,y=rating_ta)) +
  geom_point(color="deepskyblue4") + 
  stat_smooth(method="lm",color="skyblue4", fill="skyblue3") +
  labs(x="Precio por noche (MXN)", y="Evaluación de usario",
       title="Comparación entre precio y evaluación de usuario en\nTripAdvisor") +
  scale_x_continuous(breaks = seq(0,15000,500)) +
  scale_y_continuous(breaks = seq(0,10,0.5)) +
  theme(plot.title = element_text(hjust = 0.5))

# - [ ]  Boxplot de precios
aux <-paste("$",round(mean(hoteles$prices_bk),2))
ggplot(data=hoteles)+
  geom_boxplot(mapping = aes(x=prices_bk), color="deepskyblue4", fill="deepskyblue1",) + 
  labs(x="Precio por noche(MXN)",
       title="Distribución de precios por noche en\nBooking") +
  geom_point(mapping = aes(x=mean(prices_bk),y=0),fill="royalblue4", shape=23)+
  scale_x_continuous(breaks = seq(0,15000,500)) +
  theme(plot.title = element_text(hjust = 0.5))

aux <-paste("$",round(mean(hoteles[!(is.na(hoteles$prices_ta)),]$prices_ta),2))
ggplot(data=hoteles)+
  geom_boxplot(mapping = aes(x=prices_ta), color="deepskyblue4", fill="deepskyblue1",) + 
  labs(x="Precio por noche(MXN)",
       title="Distribución de precios por noche en\nBooking") +
  geom_point(mapping = aes(x=mean(hoteles[!(is.na(hoteles$prices_ta)),]$prices_ta),y=0),fill="royalblue4", shape=23)+
  scale_x_continuous(breaks = seq(0,15000,500)) +
  theme(plot.title = element_text(hjust = 0.5))

# Accesibilidad a PCC
tmp <- hoteles %>% group_by(inclusion) %>% summarize(count=n())
ggplot(tmp, aes(x = "", y = count, fill = as.factor(inclusion))) +
  geom_col(color = "black") +
  coord_polar(theta = "y",start=0) +
  geom_text(aes(label = paste(round(count/122*100,2),"%") ),
            position = position_stack(vjust = 0.5), size=3, color=c("white","black")) +
  scale_fill_manual(values=c("firebrick2","deepskyblue2"),labels=c('No','Sí'),"") +
  labs(title = "Disponibilidad de al menos un servicio para\npersonas con discapacidad") +
  theme_void()+
  theme(plot.title = element_text(hjust = 0.5))
