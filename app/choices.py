ESTADO_ENVIO = {
    ('EN_PREPARACION', 'En preparacion'),
    ('ENVIADO', 'Enviado'),
    ('ENTREGADO', 'Entregado'),
}
REGIONES_CHILE = {
    ("REGION_ARICA_PARINACOTA", "Región de Arica y Parinacota"),
    ("REGION_TARAPACA", "Región de Tarapacá"),
    ("REGION_ANTOFAGASTA", "Región de Antofagasta"),
    ("REGION_ATACAMA", "Región de Atacama"),
    ("REGION_COQUIMBO", "Región de Coquimbo"),
    ("REGION_VALPARAISO", "Región de Valparaíso"),
    ("REGION_BERNARDO_OHIGGINS", "Región del Libertador General Bernardo O'Higgins"),
    ("REGION_MAULE", "Región del Maule"),
    ("REGION_NUBLE", "Región de Ñuble"),
    ("REGION_BIOBIO", "Región del Biobío"),
    ("REGION_ARAUCANIA", "Región de La Araucanía"),
    ("REGION_LOS_RIOS", "Región de Los Ríos"),
    ("REGION_LOS_LAGOS", "Región de Los Lagos"),
    ("REGION_AISEN", "Región Aisén del General Carlos Ibáñez del Campo"),
    ("REGION_MAGALLANES", "Región de Magallanes y de la Antártica Chilena"),
    ("REGION_METROPOLITANA", "Región Metropolitana de Santiago"),
}

COMUNAS_POR_REGION = {
    "REGION_ARICA_PARINACOTA": {
        "ARICA": "Arica",
        "CAMARONES": "Camarones",
        "PUTRE": "Putre",
        "GENERAL_LAGOS": "General Lagos"
    },
    "REGION_TARAPACA": {
        "IQUIQUE": "Iquique",
        "ALTO_HOSPICIO": "Alto Hospicio",
        "POZO_ALMONTE": "Pozo Almonte",
        "CAMINA": "Camiña",
        "COLCHANE": "Colchane",
        "HUARA": "Huara",
        "PICA": "Pica"
    },
    "REGION_ANTOFAGASTA": {
        "ANTOFAGASTA": "Antofagasta",
        "MEJILLONES": "Mejillones",
        "SIERRA_GORDA": "Sierra Gorda",
        "TALTAL": "Taltal",
        "CALAMA": "Calama",
        "OLLAGUE": "Ollagüe",
        "SAN_PEDRO_ATACAMA": "San Pedro de Atacama",
        "TOCOPILLA": "Tocopilla",
        "MARIA_ELENA": "María Elena"
    },
    "REGION_ATACAMA": {
        "COPIAPO": "Copiapó",
        "CALDERA": "Caldera",
        "TIERRA_AMARILLA": "Tierra Amarilla",
        "CHANARAL": "Chañaral",
        "DIEGO_ALMAGRO": "Diego de Almagro",
        "VALLENAR": "Vallenar",
        "HUASCO": "Huasco",
        "FREIRINA": "Freirina",
        "ALTO_CARMEN": "Alto del Carmen"
    },
    "REGION_COQUIMBO": {
        "LA_SERENA": "La Serena",
        "COQUIMBO": "Coquimbo",
        "ANDACOLLO": "Andacollo",
        "LA_HIGUERA": "La Higuera",
        "PAIGUANO": "Paiguano",
        "VICUNA": "Vicuña",
        "ILLAPEL": "Illapel",
        "CANELA": "Canela",
        "LOS_VILOS": "Los Vilos",
        "SALAMANCA": "Salamanca",
        "OVALLE": "Ovalle",
        "COMBARBALA": "Combarbalá",
        "MONTE_PATRIA": "Monte Patria",
        "PUNITAQUI": "Punitaqui",
        "RIO_HURTADO": "Río Hurtado"
    },
    "REGION_VALPARAISO": {
        "VALPARAISO": "Valparaíso",
        "CASABLANCA": "Casablanca",
        "CONCON": "Concón",
        "JUAN_FERNANDEZ": "Juan Fernández",
        "PUCHUNCAVI": "Puchuncaví",
        "QUINTERO": "Quintero",
        "VINA_DEL_MAR": "Viña del Mar",
        "ISLA_DE_PASCUA": "Isla de Pascua",
        "LOS_ANDES": "Los Andes",
        "CALLE_LARGA": "Calle Larga",
        "RINCONADA": "Rinconada",
        "SAN_ESTEBAN": "San Esteban",
        "LA_LIGUA": "La Ligua",
        "CABILDO": "Cabildo",
        "PAPUDO": "Papudo",
        "PETORCA": "Petorca",
        "ZAPALLAR": "Zapallar",
        "QUILLOTA": "Quillota",
        "CALERA": "Calera",
        "HIJUELAS": "Hijuelas",
        "LA_CRUZ": "La Cruz",
        "NOGALES": "Nogales",
        "SAN_ANTONIO": "San Antonio",
        "ALGARROBO": "Algarrobo",
        "CARTAGENA": "Cartagena",
        "EL_QUISCO": "El Quisco",
        "EL_TABO": "El Tabo",
        "SANTO_DOMINGO": "Santo Domingo",
        "SAN_FELIPE": "San Felipe",
        "CATEMU": "Catemu",
        "LLAILLAY": "Llaillay",
        "PANQUEHUE": "Panquehue",
        "PUTAENDO": "Putaendo",
        "SANTA_MARIA": "Santa María",
        "QUILPUE": "Quilpué",
        "LIMACHE": "Limache",
        "OLMUE": "Olmué",
        "VILLA_ALEMANA": "Villa Alemana"
    },
    "REGION_BERNARDO_OHIGGINS": {
        "RANCAGUA": "Rancagua",
        "CODEGUA": "Codegua",
        "COINCO": "Coinco",
        "COLTAUCO": "Coltauco",
        "DONIHUE": "Doñihue",
        "GRANEROS": "Graneros",
        "LAS_CABRAS": "Las Cabras",
        "MACHALI": "Machalí",
        "MALLOA": "Malloa",
        "MOSTAZAL": "Mostazal",
        "OLIVAR": "Olivar",
        "PEUMO": "Peumo",
        "PICHIDEGUA": "Pichidegua",
        "QUINTA_DE_TILCOCO": "Quinta de Tilcoco",
        "RENGO": "Rengo",
        "REQUINOA": "Requínoa",
        "SAN_VICENTE": "San Vicente",
        "PICHILEMU": "Pichilemu",
        "LA_ESTRELLA": "La Estrella",
        "LITUECHE": "Litueche",
        "MARCHIGUE": "Marchigüe",
        "NAVIDAD": "Navidad",
        "PAREDONES": "Paredones",
        "SAN_FERNANDO": "San Fernando",
        "CHEPICA": "Chépica",
        "CHIMBARONGO": "Chimbarongo",
        "LOLOL": "Lolol",
        "NANCAGUA": "Nancagua",
        "PALMILLA": "Palmilla",
        "PERALILLO": "Peralillo",
        "PLACILLA": "Placilla",
        "PUMANQUE": "Pumanque",
        "SANTA_CRUZ": "Santa Cruz"
    },
    "REGION_MAULE": {
        "TALCA": "Talca",
        "CONSTITUCION": "Constitución",
        "CUREPTO": "Curepto",
        "EMPEDRADO": "Empedrado",
        "MAULE": "Maule",
        "PELARCO": "Pelarco",
        "PENCAHUE": "Pencahue",
        "RIO_CLARO": "Río Claro",
        "SAN_CLEMENTE": "San Clemente",
        "SAN_RAFAEL": "San Rafael",
        "CAUQUENES": "Cauquenes",
        "CHANCO": "Chanco",
        "PELLUHUE": "Pelluhue",
        "CURICO": "Curicó",
        "HUALANE": "Hualañé",
        "LICANTEN": "Licantén",
        "MOLINA": "Molina",
        "RAUCO": "Rauco",
        "ROMERAL": "Romeral",
        "SAGRADA_FAMILIA": "Sagrada Familia",
        "TENO": "Teno",
        "VICHUQUEN": "Vichuquén",
        "LINARES": "Linares",
        "COLBUN": "Colbún",
        "LONGAVI": "Longaví",
        "PARRAL": "Parral",
        "RETIRO": "Retiro",
        "SAN_JAVIER": "San Javier",
        "VILLA_ALEGRE": "Villa Alegre",
        "YERBAS_BUENAS": "Yerbas Buenas"
    },
    "REGION_NUBLE": {
        "CHILLAN": "Chillán",
        "BULNES": "Bulnes",
        "COBQUECURA": "Cobquecura",
        "COELEMU": "Coelemu",
        "COIHUECO": "Coihueco",
        "EL_CARMEN": "El Carmen",
        "NIHUE": "Ninhue",
        "NIQUEN": "Ñiquén",
        "PEMUCO": "Pemuco",
        "PINTO": "Pinto",
        "PORTEZUELO": "Portezuelo",
                "QUILLON": "Quillón",
        "QUIRIHUE": "Quirihue",
        "RANQUIL": "Ránquil",
        "SAN_CARLOS": "San Carlos",
        "SAN_FABIAN": "San Fabián",
        "SAN_NICOLAS": "San Nicolás",
        "TREGUACO": "Treguaco",
        "YUNGAY": "Yungay"
    },
    "REGION_BIOBIO": {
        "CONCEPCION": "Concepción",
        "CORONEL": "Coronel",
        "CHIGUAYANTE": "Chiguayante",
        "FLORIDA": "Florida",
        "HUALQUI": "Hualqui",
        "LOTA": "Lota",
        "PENCO": "Penco",
        "SAN_PEDRO_DE_LA_PAZ": "San Pedro de la Paz",
        "SANTA_JUANA": "Santa Juana",
        "TALCAHUANO": "Talcahuano",
        "TOME": "Tomé",
        "HUALPEN": "Hualpén",
        "LEBU": "Lebu",
        "Arauco": "Arauco",
        "Cañete": "Cañete",
        "Contulmo": "Contulmo",
        "Curanilahue": "Curanilahue",
        "Los Álamos": "Los Álamos",
        "Tirúa": "Tirúa",
        "Los Ángeles": "Los Ángeles",
        "Antuco": "Antuco",
        "Cabrero": "Cabrero",
        "Laja": "Laja",
        "Mulchén": "Mulchén",
        "Nacimiento": "Nacimiento",
        "Negrete": "Negrete",
        "Quilaco": "Quilaco",
        "Quilleco": "Quilleco",
        "San Rosendo": "San Rosendo",
        "Santa Bárbara": "Santa Bárbara",
        "Tucapel": "Tucapel",
        "Yumbel": "Yumbel",
        "Alto Biobío": "Alto Biobío"
    },
    "REGION_ARAUCANIA": {
        "Temuco": "Temuco",
        "Carahue": "Carahue",
        "Cunco": "Cunco",
        "Curarrehue": "Curarrehue",
        "Freire": "Freire",
        "Galvarino": "Galvarino",
        "Gorbea": "Gorbea",
        "Lautaro": "Lautaro",
        "Loncoche": "Loncoche",
        "Melipeuco": "Melipeuco",
        "Nueva Imperial": "Nueva Imperial",
        "Padre las Casas": "Padre las Casas",
        "Perquenco": "Perquenco",
        "Pitrufquén": "Pitrufquén",
        "Pucón": "Pucón",
        "Saavedra": "Saavedra",
        "Teodoro Schmidt": "Teodoro Schmidt",
        "Toltén": "Toltén",
        "Vilcún": "Vilcún",
        "Villarrica": "Villarrica",
        "Cholchol": "Cholchol",
        "Angol": "Angol",
        "Collipulli": "Collipulli",
        "Curacautín": "Curacautín",
        "Ercilla": "Ercilla",
        "Lonquimay": "Lonquimay",
        "Los Sauces": "Los Sauces",
        "Lumaco": "Lumaco",
        "Purén": "Purén",
        "Renaico": "Renaico",
        "Traiguén": "Traiguén",
        "Victoria": "Victoria"
    },
    "REGION_LOS_RIOS": {
        "Valdivia": "Valdivia",
        "Corral": "Corral",
        "Lanco": "Lanco",
        "Los Lagos": "Los Lagos",
        "Máfil": "Máfil",
        "Mariquina": "Mariquina",
        "Paillaco": "Paillaco",
        "Panguipulli": "Panguipulli",
        "La Unión": "La Unión",
        "Futrono": "Futrono",
        "Lago Ranco": "Lago Ranco",
        "Río Bueno": "Río Bueno"
    },
    "REGION_LOS_LAGOS": {
        "Puerto Montt": "Puerto Montt",
        "Calbuco": "Calbuco",
        "Cochamó": "Cochamó",
        "Fresia": "Fresia",
        "Frutillar": "Frutillar",
        "Los Muermos": "Los Muermos",
        "Llanquihue": "Llanquihue",
        "Maullín": "Maullín",
        "Puerto Varas": "Puerto Varas",
        "Castro": "Castro",
        "Ancud": "Ancud",
        "Chonchi": "Chonchi",
        "Curaco de Vélez": "Curaco de Vélez",
        "Dalcahue": "Dalcahue",
        "Puqueldón": "Puqueldón",
        "Queilén": "Queilén",
        "Quellón": "Quellón",
        "Quemchi": "Quemchi",
        "Quinchao": "Quinchao",
        "Osorno": "Osorno",
        "Puerto Octay": "Puerto Octay",
        "Purranque": "Purranque",
        "Puyehue": "Puyehue",
        "Río Negro": "Río Negro",
        "San Juan de la Costa": "San Juan de la Costa",
        "San Pablo": "San Pablo",
        "Chaitén": "Chaitén",
        "Futaleufú": "Futaleufú",
        "Hualaihué": "Hualaihué",
        "Palena": "Palena"
    },
    "REGION_AISEN": {
        "Coyhaique": "Coyhaique",
        "Lago Verde": "Lago Verde",
        "Aysén": "Aysén",
        "Cisnes": "Cisnes",
        "Guaitecas": "Guaitecas",
        "Cochrane": "Cochrane",
        "O'Higgins": "O'Higgins",
        "Tortel": "Tortel",
        "Chile Chico": "Chile Chico",
        "Río Ibáñez": "Río Ibáñez"
    },
    "REGION_MAGALLANES": {
        "Punta Arenas": "Punta Arenas",
        "Laguna Blanca": "Laguna Blanca",
        "Río Verde": "Río Verde",
        "San Gregorio": "San Gregorio",
        "Cabo de Hornos": "Cabo de Hornos",
        "Antártica": "Antártica",
        "Porvenir": "Porvenir",
        "Primavera": "Primavera",
        "Timaukel": "Timaukel",
        "Natales": "Natales",
        "Torres del Paine": "Torres del Paine"
    },
    "REGION_METROPOLITANA": {
        "Santiago": "Santiago",
        "Cerrillos": "Cerrillos",
        "Cerro Navia": "Cerro Navia",
        "Conchalí": "Conchalí",
        "El Bosque": "El Bosque",
        "Estación Central": "Estación Central",
        "Huechuraba": "Huechuraba",
        "Independencia": "Independencia",
        "La Cisterna": "La Cisterna",
        "La Florida": "La Florida",
        "La Granja": "La Granja",
        "La Pintana": "La Pintana",
        "La Reina": "La Reina",
        "Las Condes": "Las Condes",
        "Lo Barnechea": "Lo Barnechea",
        "Lo Espejo": "Lo Espejo",
        "Lo Prado": "Lo Prado",
        "Macul": "Macul",
        "Maipú": "Maipú",
        "Ñuñoa": "Ñuñoa",
        "Pedro Aguirre Cerda": "Pedro Aguirre Cerda",
        "Peñalolén": "Peñalolén",
        "Providencia": "Providencia",
        "Pudahuel": "Pudahuel",
        "Quilicura": "Quilicura",
        "Quinta Normal": "Quinta Normal",
        "Recoleta": "Recoleta",
        "Renca": "Renca",
        "San Joaquín": "San Joaquín",
        "San Miguel": "San Miguel",
        "San Ramón": "San Ramón",
        "Vitacura": "Vitacura"
    }
}

