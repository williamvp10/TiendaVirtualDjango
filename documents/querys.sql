DELETE FROM  public.tiendavirtualapp_clientes WHERE id < 5;
insert into public.tiendavirtualapp_clientes 
(id,nombre,apellido,correo,tipo_doc,doc_identificacion,dir_env,fecha_registro,activo,telefono) VALUES 
(1,'Daniel Julian','Barrios','daniel@gmail.com','Cc','123656785',	'Call 22 #54b 65','26-12-2020','Si','3004959285'),
(2,'Maritza','Morales','maritza@gmail.com','Cc','345366222','Call 45 #45 apto 43','26-12-2020','Si','3004959285'),
(3,'Diana','Amaya','diana@gmail.com','Cc','23456552322','Call 65 #33b apto 45','26-12-2020','Si','3004959285');

SELECT * FROM public.tiendavirtualapp_clientes
ORDER BY id ASC;

## categorias
insert into public.tiendavirtualapp_categorias
(id,codigo,nombre,descripcion,activo) VALUES
(4,'FRUTA','Fruta','Frutos comestibles obtenidos de plantas cultivadas o silvestres que, por su sabor generalmente dulce-acidulado, su aroma intenso y agradable y sus propiedades nutritivas.','Si'),
(6,'VERDU','Verdura y hortaliza','Las verduras son hortalizas cuyo color predominante es el verde, su principal aporte son las vitaminas, minerales y la fibra. No tienen apenas proteínas ni lípidos, pero sí cierta cantidad de hidratos de carbono. Son la principal fuente de vitamina A y C. La vitamina A va ligada al color amarillo o rojo, y la vitamina C al verde de las hojas.','Si'
);
SELECT * FROM public.tiendavirtualapp_categorias
ORDER BY id ASC;

## productos

insert into public.tiendavirtualapp_productos
(id,codigo,nombre,descripcion,unidad,fecha_registro,precio_unidad,fecha_precio,activo,categoria_id,imagen
) VALUES
(1,'BAN01','Bananos','La banana es un fruto comestible, botánicamente una baya, de varios tipos de grandes plantas herbáceas del género Musa. A estas plantas de gran porte que tienen aspecto de arbolillo se las denomina plataneras, bananeros, bananeras, plátanos o bananos.','Kg','26-12-2020',5000.00,'26-12-2020','Si',4,'frutas/banano.jpg'),
(2,'FRE01','Freijoa','El guayabo del país, también denominado guayabo, feijoa, guayaba o guayabo del Brasil, es una especie botánica arbustiva, ramificada, que alcanza 4 m de altura. Es originario de las tierras altas del sur de Brasil, Argentina y Uruguay. Resiste el frío, aunque no por debajo de los -12 °C','Kg','27-12-2020',2000.00,'27-12-2020','Si',4,'frutas/freijoa.jpg'),
(3,'GUA01','Guayaba','Las Guayabas son un género de unas cien especies de árboles tropicales y árboles pequeños en la familia Myrtaceae, nativas de América. Las hojas son opuestas, simples, elípticas a ovaladas, de 5 a 15 centímetros de largo. Las flores son blancas, con cinco pétalos y numerosos estambres.','Kg','27-12-2020',3000.00,'27-12-2020','Si',4,'frutas/guayaba.jpg'),
(4,'MAN01','Mandarina','La mandarina es el fruto ​ de las diferentes especies de cítricos llamados comúnmente mandarino, entre ellas Citrus reticulata, Citrus unshiu, Citrus reshni, así como sus híbridos, incluyendo Citrus × tangerina, cuya taxonomía está discutida.','Kg','27-12-2020',4000.00,'27-12-2020','Si',4,'frutas/mandarina.jpg'),
(5,'MAN01','Manzana','La manzana es el fruto comestible de la especie Malus domestica, llamada comúnmente manzano. Es una fruta pomácea de forma redonda y sabor más o menos dulce, dependiendo de la variedad. Los manzanos se cultivan en todo el mundo y son las especies más cultivadas en el género Malus.','Kg','27-12-2020',2800.00,'27-12-2020','Si',4,'frutas/manzana.jpg'),
(6,'MZV01','Manzana verde','"La manzana verde es rica en vitaminas A y E. Por ende, es rica en antioxidantes, los cuales vienen a ser importantísimos para mantener una buena salud, como exponen diversos estudios. El calcio favorece la coagulación de la sangre, además participa en la absorción de vitamina B12."','Kg','27-12-2020',3300.00,'27-12-2020','Si',4,'frutas/manzana_verde.jpg'),
(7,'NAR01','Naranja','La naranja es una fruta cítrica obtenida del naranjo dulce, del naranjo amargo y de naranjos de otras variedades o híbridos, de origen asiático.','Kg','27-12-2020',3800.00,'27-12-2020','Si',4,'frutas/naranja.jpg'),
(8,'SAN01','Sandia','Citrullus lanatus, comúnmente llamada sandía, acendría, síndria, patilla, aguamelón o melón de agua es una especie de la familia Cucurbitaceae originaria de África, pero tiene una gran presencia y difusión en Asia.','Kg','27-12-2020',6000.00,'27-12-2020','Si',4,'frutas/sandia.jpg'),
(9,'API01','Apio','Apium graveolens, llamado comúnmente apio, es una especie perteneciente a la familia de las apiáceas, de distribución cosmopolita.','Kg','27-12-2020',2000.00,'27-12-2020','Si',6,'verduras/apio.jpg'),
(10,'ARV01','Arveja','Pisum sativum es una planta herbácea de la familia de las leguminosas, más o menos trepadora, propia de la cuenca mediterránea, aunque muy extendida en todo el mundo.','Kg','27-12-2020',5000.00,'27-12-2020','Si',6,'verduras/arveja.jpg'),
(11,'BRO01','Brocoli','Brassica oleracea var. italica, el brócoli, ​ brécol​ o bróquil​ del italiano broccoli, es una planta de la familia de las brasicáceas. Otras variedades de la misma especie son el repollo, la coliflor, el colinabo y la col de Bruselas. El llamado brócoli chino o kale es también una variedad de Brassica oleracea.','Kg','27-12-2020',3500.00,'27-12-2020','Si',6,'verduras/brocoli.jpg'),
(12,'CBB01','Cebolla blanca','Allium cepa, comúnmente conocida como cebolla, es una planta herbácea bienal perteneciente a la familia de las amarilidáceas. Es la especie más cultivada del género Allium, el cual contiene varias especies que se denominan «cebollas» y que se cultivan como alimento.','Kg','27-12-2020',1500.00,'27-12-2020','Si',6,'verduras/cebolla_blanca.jpg'),
(13,'CBR01','Cebolla roja','Las Cebollas Rojas, conocidas así en Argentina, Colombia, México, Chile, Panamá, Perú, Venezuela y en Ecuador como cebolla paiteña, son cultivares de cebolla con una piel roja púrpura, y una carne blanca con maitizes rojizos. Tiende a ser de tamaño mediano a grande y a tener un sabor suave a dulce.','Kg','27-12-2020',1200.00,'27-12-2020','Si',6,'verduras/cebolla_roja.jpg'),
(14,'PIM01','Pimenton','Pues aunque lo que nos comemos del pimiento es el fruto, con sus semillas dentro, y no es de color verde, al menos cuando está maduro, sí se considera una verdura o, mejor dicho, una hortaliza.','Kg','27-12-2020',1000.00,'27-12-2020','Si',6,'verduras/pimenton.jpg'),
(15,'ZAN01','Zanahoria','Traducción del inglés-Daucus carota, cuyos nombres comunes incluyen zanahoria silvestre, nido de pájaro, encaje de obispo y encaje de la reina Ana, es una planta blanca y floreciente de la familia Apiaceae, nativa de las regiones templadas de Europa y el suroeste de Asia, y naturalizada en América del Norte y Australia.','Kg','27-12-2020',2500.00,'27-12-2020','Si',6,'verduras/zanahoria.jpg');

SELECT * FROM public.tiendavirtualapp_productos
ORDER BY id ASC;

## inventario
insert into public.tiendavirtualapp_inventario
(id,cantidad,ubicacion,precio_entrada,fecha_registro,producto_id) VALUES
(1,100,'SuB',3500.00,'26-12-2020',1),
(2,150,'NoB',1000.00,'27-12-2020',2),
(3,200,'NoB',1500.00,'27-12-2020',3),
(4,300,'NoB',3000.00,'30-12-2020',4),
(5,130,'NoB',2000.00,'30-12-2020',5),
(6,120,'NoB',2500.00,'30-12-2020',6),
(7,300,'NoB',2800.00,'30-12-2020',7),
(8,130,'NoB',4500.00,'30-12-2020',8),
(9,230,'NoB',1500.00,'30-12-2020',9),
(10,1000,'NoB',3500.00,'30-12-2020',10),
(11,140,'NoB',2400.00,'30-12-2020',11),
(12,230,'NoB',1000.00,'30-12-2020',12),
(13,200,'NoB',800.00,'30-12-2020',13),
(14,150,'NoB',500.00,'30-12-2020',14),
(15,200,'NoB',1700.00,'30-12-2020',15);
SELECT * FROM public.tiendavirtualapp_inventario
ORDER BY id ASC;

## calificaciones
insert into public.tiendavirtualapp_calificaciones 
(id,calificacion,fecha_calificacion,comentario,cliente_id,producto_id) VALUES
(1,'5','26-12-2020','Buen producto',1,1),
(2,'4','27-12-2020','exelente producto',2,1),
(3,'5','27-12-2020','exelente producto',2,2),
(4,'5','26-12-2020','me llego bien el producto',3,2),
(5,'5','26-12-2020','excelente calidad',1,2),
(6,'4','26-12-2020','buen producto',1,3),
(7,'4','28-12-2020','me gusto la presentación',	1,4);


SELECT * FROM public.tiendavirtualapp_calificaciones
ORDER BY id ASC;