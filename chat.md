# here are the results of the api tests

GET <https://consultoria-aplicada.com/wp-json/wp/v2/types>
Result:

```json
{
    "post": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Entradas",
        "slug": "post",
        "icon": "dashicons-admin-post",
        "taxonomies": [
            "category",
            "post_tag"
        ],
        "rest_base": "posts",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/posts"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "page": {
        "description": "",
        "hierarchical": true,
        "has_archive": false,
        "name": "Páginas",
        "slug": "page",
        "icon": "dashicons-admin-page",
        "taxonomies": [],
        "rest_base": "pages",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/pages"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "attachment": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Medios",
        "slug": "attachment",
        "icon": "dashicons-admin-media",
        "taxonomies": [],
        "rest_base": "media",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "nav_menu_item": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Elementos del menú de navegación",
        "slug": "nav_menu_item",
        "icon": null,
        "taxonomies": [
            "nav_menu"
        ],
        "rest_base": "menu-items",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/menu-items"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_block": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Patrones",
        "slug": "wp_block",
        "icon": null,
        "taxonomies": [
            "wp_pattern_category"
        ],
        "rest_base": "blocks",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/blocks"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_template": {
        "description": "Plantillas a incluir en tu tema.",
        "hierarchical": false,
        "has_archive": false,
        "name": "Plantillas",
        "slug": "wp_template",
        "icon": null,
        "taxonomies": [],
        "rest_base": "templates",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/templates"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_template_part": {
        "description": "Partes de plantilla a incluir en tus plantillas.",
        "hierarchical": false,
        "has_archive": false,
        "name": "Partes de plantilla",
        "slug": "wp_template_part",
        "icon": null,
        "taxonomies": [],
        "rest_base": "template-parts",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/template-parts"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_global_styles": {
        "description": "Estilos globales para incluir en los temas.",
        "hierarchical": false,
        "has_archive": false,
        "name": "Estilos globales",
        "slug": "wp_global_styles",
        "icon": null,
        "taxonomies": [],
        "rest_base": "global-styles",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/global-styles"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_navigation": {
        "description": "Menús de navegación que se pueden insertar en tu sitio.",
        "hierarchical": false,
        "has_archive": false,
        "name": "Menús de navegación",
        "slug": "wp_navigation",
        "icon": null,
        "taxonomies": [],
        "rest_base": "navigation",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/navigation"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_font_family": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Familias de fuentes",
        "slug": "wp_font_family",
        "icon": null,
        "taxonomies": [],
        "rest_base": "font-families",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/font-families"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "wp_font_face": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Fuentes",
        "slug": "wp_font_face",
        "icon": null,
        "taxonomies": [],
        "rest_base": "font-families/(?P<font_family_id>[\\d]+)/font-faces",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/font-families/(/?P<font_family_id>[\\d]+)/font-faces"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "e-floating-buttons": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Elementos flotantes",
        "slug": "e-floating-buttons",
        "icon": null,
        "taxonomies": [],
        "rest_base": "e-floating-buttons",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/e-floating-buttons"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "elementor_library": {
        "description": "",
        "hierarchical": false,
        "has_archive": false,
        "name": "Mis plantillas",
        "slug": "elementor_library",
        "icon": "dashicons-admin-page",
        "taxonomies": [],
        "rest_base": "elementor_library",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/elementor_library"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "stm_service": {
        "description": "",
        "hierarchical": false,
        "has_archive": true,
        "name": "Servicios",
        "slug": "stm_service",
        "icon": "dashicons-clipboard",
        "taxonomies": [
            "stm_service_category"
        ],
        "rest_base": "servicios",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/servicios"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "stm_staff": {
        "description": "",
        "hierarchical": false,
        "has_archive": true,
        "name": "Consultores",
        "slug": "stm_staff",
        "icon": "dashicons-id",
        "taxonomies": [],
        "rest_base": "equipo",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    "stm_testimonials": {
        "description": "",
        "hierarchical": false,
        "has_archive": true,
        "name": "Testimoniales",
        "slug": "stm_testimonials",
        "icon": "dashicons-clipboard",
        "taxonomies": [],
        "rest_base": "testimoniales",
        "rest_namespace": "wp/v2",
        "template": [],
        "template_lock": false,
        "_links": {
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types"
                }
            ],
            "wp:items": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/testimoniales"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    }
}
```

GET <https://consultoria-aplicada.com/wp-json/wp/v2/stm_staff>

correct endpoint is (remember @file config.py ENDPOINT_MAP):

GET <https://consultoria-aplicada.com/wp-json/wp/v2/equipo>
Result:

```json
[
    {
        "id": 9334,
        "date": "2025-01-12T15:45:14",
        "date_gmt": "2025-01-12T21:45:14",
        "guid": {
            "rendered": "https://consultoria-aplicada.com/?post_type=stm_staff&#038;p=9334"
        },
        "modified": "2025-04-11T00:44:37",
        "modified_gmt": "2025-04-11T06:44:37",
        "slug": "ruth-ileana-varela-alonzo",
        "status": "publish",
        "type": "stm_staff",
        "link": "https://consultoria-aplicada.com/equipo/ruth-ileana-varela-alonzo/",
        "title": {
            "rendered": "Ruth Ileana Varela Alonzo"
        },
        "content": {
            "rendered": "",
            "protected": false
        },
        "excerpt": {
            "rendered": "<p>Ruth Varela es una consultora especializada en sistematización de experiencias, facilitación de procesos metodológicos y desarrollo organizacional. Con más de 20 años de experiencia, ha colaborado con organismos internacionales, gobiernos y organizaciones civiles en América Latina, destacando por su capacidad para transformar aprendizajes en conocimiento útil y aplicable.</p>\n",
            "protected": false
        },
        "featured_media": 9335,
        "template": "",
        "class_list": [
            "post-9334",
            "stm_staff",
            "type-stm_staff",
            "status-publish",
            "has-post-thumbnail",
            "hentry"
        ],
        "acf": {
            "experiencia": "<ul>\n<li>Sistematización de Experiencias y <a href=\"https://consultoria-aplicada.com/servicios/gestion-del-conocimiento/\">Gestión del Conocimiento</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicio/facilitacion-de-procesos-participativos/\">Facilitación de Procesos Metodológicos y Participativos</a></li>\n<li><a href=\"https://consultoria-aplicada.com/desarrollo-organizacional/\">Desarrollo Social y Organizacional</a></li>\n</ul>\n",
            "educacion": "<ul>\n<li>Posgrado en Gestión por Competencias y Metodologías Participativas — Organización Internacional del Trabajo (OIT/DELNET)</li>\n<li>Licenciatura en Psicología — Universidad Nacional Autónoma de Honduras</li>\n</ul>\n",
            "extra": "<p>A lo largo de su trayectoria, Ruth ha liderado proyectos de sistematización y facilitación en áreas como desarrollo juvenil, género, seguridad alimentaria y manejo de cuencas, colaborando con instituciones como la <a href=\"https://www.giz.de/en/worldwide/153585.html\" target=\"_blank\" rel=\"noopener\">Agencia de Cooperación Internacional Alemana (GIZ)</a>, <a href=\"https://www.unwomen.org/es\" target=\"_blank\" rel=\"noopener\">ONU Mujeres</a>, <a href=\"https://www.care.org/\" target=\"_blank\" rel=\"noopener\">CARE</a> y <a href=\"https://www.swisscontact.org/es/paises/honduras\" target=\"_blank\" rel=\"noopener\">Swisscontact</a>. Su experiencia incluye la documentación de procesos complejos, la capacitación en metodologías participativas y la gestión del conocimiento, contribuyendo al fortalecimiento de organizaciones y a la implementación de estrategias sostenibles en Honduras y la región.</p>\n"
        },
        "acf_experiencia": "<ul>\n<li>Sistematización de Experiencias y <a href=\"https://consultoria-aplicada.com/servicios/gestion-del-conocimiento/\">Gestión del Conocimiento</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicio/facilitacion-de-procesos-participativos/\">Facilitación de Procesos Metodológicos y Participativos</a></li>\n<li><a href=\"https://consultoria-aplicada.com/desarrollo-organizacional/\">Desarrollo Social y Organizacional</a></li>\n</ul>\n",
        "acf_educacion": "<ul>\n<li>Posgrado en Gestión por Competencias y Metodologías Participativas — Organización Internacional del Trabajo (OIT/DELNET)</li>\n<li>Licenciatura en Psicología — Universidad Nacional Autónoma de Honduras</li>\n</ul>\n",
        "acf_extra": "<p>A lo largo de su trayectoria, Ruth ha liderado proyectos de sistematización y facilitación en áreas como desarrollo juvenil, género, seguridad alimentaria y manejo de cuencas, colaborando con instituciones como la <a href=\"https://www.giz.de/en/worldwide/153585.html\" target=\"_blank\" rel=\"noopener\">Agencia de Cooperación Internacional Alemana (GIZ)</a>, <a href=\"https://www.unwomen.org/es\" target=\"_blank\" rel=\"noopener\">ONU Mujeres</a>, <a href=\"https://www.care.org/\" target=\"_blank\" rel=\"noopener\">CARE</a> y <a href=\"https://www.swisscontact.org/es/paises/honduras\" target=\"_blank\" rel=\"noopener\">Swisscontact</a>. Su experiencia incluye la documentación de procesos complejos, la capacitación en metodologías participativas y la gestión del conocimiento, contribuyendo al fortalecimiento de organizaciones y a la implementación de estrategias sostenibles en Honduras y la región.</p>\n",
        "_links": {
            "self": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9334",
                    "targetHints": {
                        "allow": [
                            "GET",
                            "POST",
                            "PUT",
                            "PATCH",
                            "DELETE"
                        ]
                    }
                }
            ],
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
                }
            ],
            "about": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types/stm_staff"
                }
            ],
            "version-history": [
                {
                    "count": 1,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9334/revisions"
                }
            ],
            "predecessor-version": [
                {
                    "id": 9337,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9334/revisions/9337"
                }
            ],
            "wp:featuredmedia": [
                {
                    "embeddable": true,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media/9335"
                }
            ],
            "wp:attachment": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media?parent=9334"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    {
        "id": 9330,
        "date": "2025-01-12T15:35:48",
        "date_gmt": "2025-01-12T21:35:48",
        "guid": {
            "rendered": "https://consultoria-aplicada.com/?post_type=stm_staff&#038;p=9330"
        },
        "modified": "2025-04-11T00:45:00",
        "modified_gmt": "2025-04-11T06:45:00",
        "slug": "diana-marcela-landa-vayona",
        "status": "publish",
        "type": "stm_staff",
        "link": "https://consultoria-aplicada.com/equipo/diana-marcela-landa-vayona/",
        "title": {
            "rendered": "Diana Marcela Landa Vayona"
        },
        "content": {
            "rendered": "",
            "protected": false
        },
        "excerpt": {
            "rendered": "<p>Diana Landa Vayona es una especialista en comunicación para el desarrollo con más de 10 años de experiencia en la gestión de estrategias comunicacionales y facilitación de procesos participativos. Su capacidad de conectar equipos con los objetivos del proyecto ha generado impacto en sectores públicos, privados y de cooperación internacional.</p>\n",
            "protected": false
        },
        "featured_media": 9331,
        "template": "",
        "class_list": [
            "post-9330",
            "stm_staff",
            "type-stm_staff",
            "status-publish",
            "has-post-thumbnail",
            "hentry"
        ],
        "acf": {
            "experiencia": "<ul>\n<li><a href=\"https://consultoria-aplicada.com/servicio/facilitacion-de-procesos-participativos/\">Facilitación de Procesos Participativos</a></li>\n<li>Comunicación para el Desarrollo</li>\n<li>Diseño e Implementación de Estrategias de Comunicación</li>\n</ul>\n",
            "educacion": "<ul>\n<li>Maestría en Gestión del Desarrollo con Abordaje Psicosocial —<br />\nUniversidad José Cecilio del Valle, Tegucigalpa, Honduras</li>\n<li>Licenciatura en Periodismo — Universidad Nacional Autónoma de Honduras</li>\n</ul>\n",
            "extra": "<p>Diana ha liderado procesos de comunicación estratégica y facilitación en proyectos con organismos como la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID), la <a href=\"https://www.eda.admin.ch/deza/es/home.html\" target=\"_blank\" rel=\"noopener\">Agencia Suiza para el Desarrollo y la Cooperación (COSUDE)</a> y la <a href=\"https://www.eeas.europa.eu/delegations/honduras_es?s=188\" target=\"_blank\" rel=\"noopener\">Unión Europea</a>, trabajando en sectores como el desarrollo rural, el cacao, la educación y el empoderamiento de comunidades. Su experiencia abarca desde la producción de materiales educativos y visibilidad institucional hasta la coordinación de eventos nacionales y regionales. Ha destacado por su habilidad para transformar la comunicación en una herramienta clave para el desarrollo sostenible y el fortalecimiento organizacional.</p>\n"
        },
        "acf_experiencia": "<ul>\n<li><a href=\"https://consultoria-aplicada.com/servicio/facilitacion-de-procesos-participativos/\">Facilitación de Procesos Participativos</a></li>\n<li>Comunicación para el Desarrollo</li>\n<li>Diseño e Implementación de Estrategias de Comunicación</li>\n</ul>\n",
        "acf_educacion": "<ul>\n<li>Maestría en Gestión del Desarrollo con Abordaje Psicosocial —<br />\nUniversidad José Cecilio del Valle, Tegucigalpa, Honduras</li>\n<li>Licenciatura en Periodismo — Universidad Nacional Autónoma de Honduras</li>\n</ul>\n",
        "acf_extra": "<p>Diana ha liderado procesos de comunicación estratégica y facilitación en proyectos con organismos como la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID), la <a href=\"https://www.eda.admin.ch/deza/es/home.html\" target=\"_blank\" rel=\"noopener\">Agencia Suiza para el Desarrollo y la Cooperación (COSUDE)</a> y la <a href=\"https://www.eeas.europa.eu/delegations/honduras_es?s=188\" target=\"_blank\" rel=\"noopener\">Unión Europea</a>, trabajando en sectores como el desarrollo rural, el cacao, la educación y el empoderamiento de comunidades. Su experiencia abarca desde la producción de materiales educativos y visibilidad institucional hasta la coordinación de eventos nacionales y regionales. Ha destacado por su habilidad para transformar la comunicación en una herramienta clave para el desarrollo sostenible y el fortalecimiento organizacional.</p>\n",
        "_links": {
            "self": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9330",
                    "targetHints": {
                        "allow": [
                            "GET",
                            "POST",
                            "PUT",
                            "PATCH",
                            "DELETE"
                        ]
                    }
                }
            ],
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
                }
            ],
            "about": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types/stm_staff"
                }
            ],
            "version-history": [
                {
                    "count": 4,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9330/revisions"
                }
            ],
            "predecessor-version": [
                {
                    "id": 10115,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9330/revisions/10115"
                }
            ],
            "wp:featuredmedia": [
                {
                    "embeddable": true,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media/9331"
                }
            ],
            "wp:attachment": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media?parent=9330"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    {
        "id": 9326,
        "date": "2025-01-12T14:28:05",
        "date_gmt": "2025-01-12T20:28:05",
        "guid": {
            "rendered": "https://consultoria-aplicada.com/?post_type=stm_staff&#038;p=9326"
        },
        "modified": "2025-04-11T00:45:22",
        "modified_gmt": "2025-04-11T06:45:22",
        "slug": "rosa-angela-morales-betanco",
        "status": "publish",
        "type": "stm_staff",
        "link": "https://consultoria-aplicada.com/equipo/rosa-angela-morales-betanco/",
        "title": {
            "rendered": "Rosa Ángela Morales Betanco"
        },
        "content": {
            "rendered": "",
            "protected": false
        },
        "excerpt": {
            "rendered": "<p>Con más de una década de experiencia, Ángela Morales se destaca en la planificación estratégica y la dirección de proyectos en sectores como la energía renovable, las instituciones financieras y la educación. Su enfoque holístico, meticulosa atención al detalle y habilidad para liderar procesos complejos han generado soluciones que promueven el crecimiento organizacional.</p>\n",
            "protected": false
        },
        "featured_media": 9327,
        "template": "",
        "class_list": [
            "post-9326",
            "stm_staff",
            "type-stm_staff",
            "status-publish",
            "has-post-thumbnail",
            "hentry"
        ],
        "acf": {
            "experiencia": "<ul>\n<li><a href=\"https://consultoria-aplicada.com/servicio/planificacion-estrategica/\">Planificación Estratégica</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicio/evaluacion-y-sistematizacion-de-proyectos/\">Administración de Proyectos</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicios/transformacion-cultural/\">Gestión del Cambio</a></li>\n</ul>\n",
            "educacion": "<ul>\n<li>Maestría en Administración de Proyectos (Magna Cum Laude)<br />\n— UNITEC, Tegucigalpa, Honduras</li>\n<li>Licenciatura en Administración Industrial y de Negocios —<br />\nUNITEC, Tegucigalpa, Honduras</li>\n<li>Certificación en Project Management for Development Professional (PMD Pro1)</li>\n</ul>\n",
            "extra": "<p>Ángela ha liderado proyectos estratégicos en América Latina, colaborando con instituciones públicas y privadas como la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) en América Latina y el Caribe, el <a href=\"https://www.iadb.org/es\" target=\"_blank\" rel=\"noopener\">Banco Interamericano de Desarrollo (BID)</a>, Digicel y el <a href=\"https://bancopopular.hn/\">Banco Popular</a>. Su experiencia incluye la implementación de metodologías internacionales como las del <a href=\"https://www.pmi.org/\" target=\"_blank\" rel=\"noopener\">Project Management Institute (PMI)</a> y <a href=\"https://www.tenstep.com/\" target=\"_blank\" rel=\"noopener\">TenStep</a>. Su enfoque en involucrar al liderazgo en los procesos de planificación ha impulsado la transformación de múltiples equipos e instituciones.</p>\n"
        },
        "acf_experiencia": "<ul>\n<li><a href=\"https://consultoria-aplicada.com/servicio/planificacion-estrategica/\">Planificación Estratégica</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicio/evaluacion-y-sistematizacion-de-proyectos/\">Administración de Proyectos</a></li>\n<li><a href=\"https://consultoria-aplicada.com/servicios/transformacion-cultural/\">Gestión del Cambio</a></li>\n</ul>\n",
        "acf_educacion": "<ul>\n<li>Maestría en Administración de Proyectos (Magna Cum Laude)<br />\n— UNITEC, Tegucigalpa, Honduras</li>\n<li>Licenciatura en Administración Industrial y de Negocios —<br />\nUNITEC, Tegucigalpa, Honduras</li>\n<li>Certificación en Project Management for Development Professional (PMD Pro1)</li>\n</ul>\n",
        "acf_extra": "<p>Ángela ha liderado proyectos estratégicos en América Latina, colaborando con instituciones públicas y privadas como la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) en América Latina y el Caribe, el <a href=\"https://www.iadb.org/es\" target=\"_blank\" rel=\"noopener\">Banco Interamericano de Desarrollo (BID)</a>, Digicel y el <a href=\"https://bancopopular.hn/\">Banco Popular</a>. Su experiencia incluye la implementación de metodologías internacionales como las del <a href=\"https://www.pmi.org/\" target=\"_blank\" rel=\"noopener\">Project Management Institute (PMI)</a> y <a href=\"https://www.tenstep.com/\" target=\"_blank\" rel=\"noopener\">TenStep</a>. Su enfoque en involucrar al liderazgo en los procesos de planificación ha impulsado la transformación de múltiples equipos e instituciones.</p>\n",
        "_links": {
            "self": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9326",
                    "targetHints": {
                        "allow": [
                            "GET",
                            "POST",
                            "PUT",
                            "PATCH",
                            "DELETE"
                        ]
                    }
                }
            ],
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
                }
            ],
            "about": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types/stm_staff"
                }
            ],
            "version-history": [
                {
                    "count": 4,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9326/revisions"
                }
            ],
            "predecessor-version": [
                {
                    "id": 10114,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/9326/revisions/10114"
                }
            ],
            "wp:featuredmedia": [
                {
                    "embeddable": true,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media/9327"
                }
            ],
            "wp:attachment": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media?parent=9326"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    },
    {
        "id": 7540,
        "date": "2024-11-23T01:23:01",
        "date_gmt": "2024-11-23T07:23:01",
        "guid": {
            "rendered": "https://consultoria-aplicada.com/staff/alfredo-enrique-umana/"
        },
        "modified": "2025-04-11T15:34:06",
        "modified_gmt": "2025-04-11T21:34:06",
        "slug": "alfredo-enrique-umana",
        "status": "publish",
        "type": "stm_staff",
        "link": "https://consultoria-aplicada.com/equipo/alfredo-enrique-umana/",
        "title": {
            "rendered": "Alfredo Enrique Umaña"
        },
        "content": {
            "rendered": "\t\t<div data-elementor-type=\"wp-post\" data-elementor-id=\"7540\" class=\"elementor elementor-7540 elementor-461\" data-elementor-post-type=\"stm_staff\">\n\t\t\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-aa6622c elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"aa6622c\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-aa6676e\" data-id=\"aa6676e\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-aa66bd4 elementor-widget elementor-widget-vc_custom_heading\" data-id=\"aa66bd4\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading capitalize consulting_heading_font  text_align_left has_subtitle\" ><h2 style=\"text-align: left;font-weight:700\" class=\"consulting-custom-title\">Alfredo Enrique Umaña<span class=\"subtitle\">Fundador y Consultor Principal</span></h2></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-e63b71f e-flex e-con-boxed e-con e-parent\" data-id=\"e63b71f\" data-element_type=\"container\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t<div class=\"e-con-inner\">\n\t\t<div class=\"elementor-element elementor-element-249fc9a e-con-full e-flex e-con e-child\" data-id=\"249fc9a\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-82caa28 img-box-shadow elementor-widget elementor-widget-image\" data-id=\"82caa28\" data-element_type=\"widget\" data-widget_type=\"image.default\">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<img fetchpriority=\"high\" decoding=\"async\" width=\"1024\" height=\"1024\" src=\"https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1024x1024.jpeg\" class=\"attachment-large size-large wp-image-7534\" alt=\"Alfredo Enrique Umaña Martínez\" srcset=\"https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1024x1024.jpeg 1024w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-300x300.jpeg 300w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-150x150.jpeg 150w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-768x768.jpeg 768w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1536x1536.jpeg 1536w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-2048x2048.jpeg 2048w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-50x50.jpeg 50w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-320x320.jpeg 320w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-900x900.jpeg 900w\" sizes=\"(max-width: 1024px) 100vw, 1024px\" />\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-35395d2 e-con-full e-flex e-con e-child\" data-id=\"35395d2\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-5dd9c5d elementor-widget elementor-widget-vc_custom_heading\" data-id=\"5dd9c5d\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><div style=\"font-size: 16px;color: #222222;text-align: left;line-height: 22px;font-weight:700\" class=\"consulting-custom-title\">áreas de experiencia\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-8ce9f5c elementor-widget elementor-widget-text-editor\" data-id=\"8ce9f5c\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<ul style=\"font-size: 13px; line-height: 18px;\">\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Desarrollo Organizacional</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Manejo del Cambio</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Compression Planning</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Estrategias de Crecimiento</span></li>\n</ul>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-59abb71 e-con-full e-flex e-con e-child\" data-id=\"59abb71\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-2de6f3f elementor-widget elementor-widget-vc_custom_heading\" data-id=\"2de6f3f\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><div style=\"font-size: 16px;color: #222222;text-align: left;line-height: 22px;font-weight:700\" class=\"consulting-custom-title\">educación\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-8e2927f elementor-widget elementor-widget-text-editor\" data-id=\"8e2927f\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<ul style=\"font-size: 13px; line-height: 18px;\">\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Máster en Administración de Empresas, Instituto Centroamericano de Administración de Empresas — INCAE</span></li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\"><span style=\"color: #002e5b;\">Licenciado en Administración de Empresas, Universidad Nacional Autónoma de Honduras</span></li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\">MBA, Rotterdam School of Management, Erasmus University</li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\"> </li>\n</ul>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68855 easy-read elementor-widget elementor-widget-text-editor\" data-id=\"aa68855\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>La distintiva metodología de Alfredo Enrique Umaña en el fortalecimiento organizacional se ha consolidado como referente regional tras veinte años de trayectoria, integrando innovación estratégica con rigurosa medición de resultados. Su excepcional capacidad para potenciar equipos directivos y optimizar estructuras operacionales lo posiciona como asesor estratégico de confianza para corporaciones e instituciones sin fines de lucro. Su propuesta de valor se distingue por catalizar transformaciones organizacionales profundas y sostenibles, generando impacto tangible y cuantificable en los indicadores clave de desempeño de sus clientes.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68a77 elementor-widget elementor-widget-text-editor\" data-id=\"aa68a77\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<blockquote>\n<p>Consultoría Aplicada pone a disposición de sus clientes los talentos, habilidades y experiencia profesional de nuestros consultores, quienes brindan un enorme aporte al logro de las metas transformadoras de los procesos de los servicios que ofrecemos.</p>\n</blockquote>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68c97 elementor-widget elementor-widget-text-editor\" data-id=\"aa68c97\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>Antes de fundar Consultoría Aplicaa, Alfredo manejó posiciones de dirección en importantes empresas locales y transnacionales, en las que brindó enormes aportes en el desarrollo de su desempeño.</p>\n<p>Como ávido consumidor de conocimiento y creador de contenido relevante para el crecimiento y mejora empresarial, Alfredo también comparte periódicamente sus acertados consejos en múltiples publicaciones en nuestro blog, carta de noticias y redes sociales.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-c736f70 elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"c736f70\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-8a8a120\" data-id=\"8a8a120\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-43fb74c elementor-widget elementor-widget-vc_custom_heading\" data-id=\"43fb74c\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading no_stripe consulting_heading_font  text_align_left\" ><h4 style=\"color: #222222;text-align: left;font-weight:700\" class=\"consulting-custom-title\">publicaciones\n</h4></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-0720fcc img-box-shadow elementor-widget elementor-widget-stm_news\" data-id=\"0720fcc\" data-element_type=\"widget\" data-widget_type=\"stm_news.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\t\t\t\t<div class=\"consulting_posts_box consulting_elementor_posts\n\t\t\t\tgrid\t\t\t\t\">\n\t\t\t\t\t<ul class=\"consulting_posts posts_per_row_2\">\n\t\t\t\t\t\t<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2025/03/Renovacion-Empresarial-350x250.jpg' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\">Renovación empresarial: Cómo evitar el deterioro silencioso</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/gestion-del-cambio/\" class=\"category category-1\">Gestión del Cambio</a>, <a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-2\">Lecciones Empresariales</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Al igual que una casa, una empresa necesita mantenimiento constante para no perder su propósito ni pertinencia. Descubre cómo renovar tu negocio para que vuelva a brillar.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">marzo 18, 2025</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2024/12/ahora-lo-vimos-350x250.png' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\">Cómo convertir un año difícil en la base para un éxito futuro</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/estrategias-de-reaccion-rapida/\" class=\"category category-1\">Estrategias de Reacción Rápida</a>, <a href=\"https://consultoria-aplicada.com/categoria/gestion-del-cambio/\" class=\"category category-2\">Gestión del Cambio</a><a href=\"https://consultoria-aplicada.com/categoria/innovacion-en-crisis/\" class=\"category category-3\">Innovación en Crisis</a><a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-4\">Lecciones Empresariales</a><a href=\"https://consultoria-aplicada.com/categoria/lidesazgo-estrategico/\" class=\"category category-5\">Lidesazgo Estratégico</a><a href=\"https://consultoria-aplicada.com/categoria/productividad-y-planificacion/\" class=\"category category-6\">Productividad y Planificación</a><a href=\"https://consultoria-aplicada.com/categoria/resiliencia-organizacional/\" class=\"category category-7\">Resiliencia Organizacional</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Cuando enfrentamos desafíos inesperados, también encontramos lecciones valiosas. Aprende cómo convertir las dificultades en estrategias efectivas para avanzar con claridad, creatividad y compromiso.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">diciembre 4, 2024</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2025/02/Sorprende-a-tus-clientes-350x250.jpg' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\">¡Sorprende a tus clientes y ellos te sorprenderán a ti!</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/innovacion/\" class=\"category category-1\">Innovación</a>, <a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-2\">Lecciones Empresariales</a><a href=\"https://consultoria-aplicada.com/categoria/productividad-y-planificacion/\" class=\"category category-3\">Productividad y Planificación</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Tres paradigmas transformadores para el servicio al cliente: abundancia vs. escasez, sastre vs. tienda, y destino vs. taxímetro. Descubra cómo superar expectativas desde una mentalidad de servicio genuino genera lealtad duradera y convierte relaciones comerciales en alianzas estratégicas.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">noviembre 29, 2024</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-10daa0a elementor-widget elementor-widget-stm_staff_bottom\" data-id=\"10daa0a\" data-element_type=\"widget\" data-widget_type=\"stm_staff_bottom.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\"staff_bottom_wr consulting_elementor_staff_bottom\">\n    <div class=\"staff_bottom\">\n\t<h4 class=\"no_stripe\">detalles de contacto</h4>\n\t<div class=\"infos\">\n\t\t<div class=\"info\">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"info\">\n\t\t\t<div class=\"socials\">\n\t\t\t\t<p>Perfiles Sociales</p>\n\t\t\t\t<ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-b570414 elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"b570414\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-25 elementor-top-column elementor-element elementor-element-918aa26\" data-id=\"918aa26\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-e0ecff8 elementor-widget elementor-widget-vc_custom_heading\" data-id=\"e0ecff8\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><h4 style=\"text-align: left;font-weight:700\" class=\"consulting-custom-title\">contacto\n</h4></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-90783fc elementor-widget elementor-widget-text-editor\" data-id=\"90783fc\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>Si tienes una consulta, no dudes en contactarnos.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t<div class=\"elementor-column elementor-col-75 elementor-top-column elementor-element elementor-element-3a45629\" data-id=\"3a45629\" data-element_type=\"column\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-5db975e elementor-widget elementor-widget-stm_contact_form_7\" data-id=\"5db975e\" data-element_type=\"widget\" data-widget_type=\"stm_contact_form_7.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\n<div class=\"wpcf7 no-js\" id=\"wpcf7-f8238-o1\" lang=\"es-ES\" dir=\"ltr\" data-wpcf7-id=\"8238\">\n<div class=\"screen-reader-response\"><p role=\"status\" aria-live=\"polite\" aria-atomic=\"true\"></p> <ul></ul></div>\n<form action=\"/wp-json/wp/v2/equipo#wpcf7-f8238-o1\" method=\"post\" class=\"wpcf7-form init\" aria-label=\"Formulario de contacto\" novalidate=\"novalidate\" data-status=\"init\">\n<div style=\"display: none;\">\n<input type=\"hidden\" name=\"_wpcf7\" value=\"8238\" />\n<input type=\"hidden\" name=\"_wpcf7_version\" value=\"6.0.6\" />\n<input type=\"hidden\" name=\"_wpcf7_locale\" value=\"es_ES\" />\n<input type=\"hidden\" name=\"_wpcf7_unit_tag\" value=\"wpcf7-f8238-o1\" />\n<input type=\"hidden\" name=\"_wpcf7_container_post\" value=\"0\" />\n<input type=\"hidden\" name=\"_wpcf7_posted_data_hash\" value=\"\" />\n<input type=\"hidden\" name=\"_wpcf7_recaptcha_response\" value=\"\" />\n</div>\n<div class=\"member_feedback\">\n    <div class=\"row\">\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"nombres\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Nombres\" value=\"\" type=\"text\" name=\"nombres\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"apellidos\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Apellidos\" value=\"\" type=\"text\" name=\"apellidos\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"email\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-email wpcf7-validates-as-required wpcf7-text wpcf7-validates-as-email\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Correo Electrónico\" value=\"\" type=\"email\" name=\"email\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"tel\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-tel wpcf7-text wpcf7-validates-as-tel\" aria-invalid=\"false\" placeholder=\"Teléfono\" value=\"\" type=\"tel\" name=\"tel\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"ciudad\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Ciudad\" value=\"\" type=\"text\" name=\"ciudad\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"estado\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text\" aria-invalid=\"false\" placeholder=\"Estado, Departamento o Provincia\" value=\"\" type=\"text\" name=\"estado\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"pais\"><select class=\"wpcf7-form-control wpcf7-select\" aria-invalid=\"false\" name=\"pais\"><option value=\"\">Honduras</option><option value=\"Argentina\">Argentina</option><option value=\"Belice\">Belice</option><option value=\"Bolivia\">Bolivia</option><option value=\"Canadá\">Canadá</option><option value=\"Chile\">Chile</option><option value=\"Colombia\">Colombia</option><option value=\"Costa Rica\">Costa Rica</option><option value=\"Cuba\">Cuba</option><option value=\"Dominicana\">Dominicana</option><option value=\"Ecuador\">Ecuador</option><option value=\"El Salvador\">El Salvador</option><option value=\"Estados Unidos de América\">Estados Unidos de América</option><option value=\"Guatemala\">Guatemala</option><option value=\"México\">México</option><option value=\"Nicaragua\">Nicaragua</option><option value=\"Panamá\">Panamá</option><option value=\"Paraguay\">Paraguay</option><option value=\"Perú\">Perú</option><option value=\"Puerto Rico\">Puerto Rico</option><option value=\"Uruguay\">Uruguay</option><option value=\"Venezuela\">Venezuela</option><option value=\"Otro\">Otro</option></select></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n               <button type=\"submit\" class=\"button size-lg icon_right\">ENVIAR<i class=\"fa fa-chevron-right\"></i></button>\n            </div>\n        </div>\n    </div>\n</div><p style=\"display: none !important;\" class=\"akismet-fields-container\" data-prefix=\"_wpcf7_ak_\"><label>&#916;<textarea name=\"_wpcf7_ak_hp_textarea\" cols=\"45\" rows=\"8\" maxlength=\"100\"></textarea></label><input type=\"hidden\" id=\"ak_js_1\" name=\"_wpcf7_ak_js\" value=\"204\"/><script>document.getElementById( \"ak_js_1\" ).setAttribute( \"value\", ( new Date() ).getTime() );</script></p><div class=\"wpcf7-response-output\" aria-hidden=\"true\"></div>\n</form>\n</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t<div class=\"elementor-element elementor-element-d63bf4f third_bg_color e-flex e-con-boxed e-con e-parent\" data-id=\"d63bf4f\" data-element_type=\"container\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t<div class=\"e-con-inner\">\n\t\t<div class=\"elementor-element elementor-element-75d4c2f e-con-full e-flex e-con e-child\" data-id=\"75d4c2f\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-0f41895 elementor-widget elementor-widget-vc_cta\" data-id=\"0f41895\" data-element_type=\"widget\" data-widget_type=\"vc_cta.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\n<div class=\"ce_cta ce_cta_f6c2cc24f9f259f1bb160a808fcc31f7 ce_text_left third_bg_color add_button_right btn_align_right btn_button_block_true btn_has_icon btn_has_icon_on_the_right\" id=\"\">\n\t<div class=\"ce_cta__content\">\n\t\t<div class=\"ce_cta__content__header\">\n\t\t\t<h2  class='ce_cta__content__title '>¿Necesitas una consultoría de primer nivel para tu empresa?</h2>\t\t</div>\n\t\t\t</div>\n\n\t\t<div class=\"ce_cta__action\">\n\t\t<a\n\t\t\thref=\"#\"\n\t\t\t\t\t\ttarget=\"_self\"\n\t\t\tclass=\"button\n\t\t\t\t\t\">\n\t\t\t<span>solicitar propuesta</span>\n\t\t\t\t\t\t<i class=\"fa fa-chevron-right\"></i>\n\t\t\t\t\t</a>\n\t</div>\n\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t",
            "protected": false
        },
        "excerpt": {
            "rendered": "<p>La distintiva metodología de Alfredo Enrique Umaña en el fortalecimiento organizacional se ha consolidado como referente regional tras veinte años de trayectoria, integrando innovación estratégica con rigurosa medición de resultados. Su excepcional capacidad para potenciar equipos directivos y optimizar estructuras operacionales lo posiciona como asesor estratégico de confianza para corporaciones e instituciones sin fines de lucro. Su propuesta de valor se distingue por catalizar transformaciones organizacionales profundas y sostenibles, generando impacto tangible y cuantificable en los indicadores clave de desempeño de sus clientes.</p>\n",
            "protected": false
        },
        "featured_media": 7534,
        "template": "",
        "class_list": [
            "post-7540",
            "stm_staff",
            "type-stm_staff",
            "status-publish",
            "has-post-thumbnail",
            "hentry"
        ],
        "acf": [],
        "acf_experiencia": "<ul>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/planificacion-estrategica/\">Planificación Estratégica</a></li>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/formacion-corporativa/\">Formación Corporativa</a></li>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/coaching-ejecutivo-avanzado/\">Coaching Ejecutivo</a></li>\r\n</ul>",
        "acf_educacion": "<ul>\r\n \t<li>Maestría en Administración de Empresas (MBA) — INCAE, Alajuela, Costa Rica</li>\r\n \t<li>Especialización en Liderazgo e Inteligencia Emocional — Trinity University, Chicago, IL, USA</li>\r\n \t<li>Certificación en Planificación Visual — Compression Planning Institute, Pittsburgh, PA, USA</li>\r\n</ul>",
        "acf_extra": "Alfredo inició su trayectoria profesional como consultor en <a href=\"https://www2.deloitte.com/hn/es.html\" target=\"_blank\" rel=\"noopener\">Deloitte &amp; Touche Business Solutions S.A.</a>, después de haber ocupado roles gerenciales en diversas industrias. Entre estas, destacan su experiencia en el sector de combustibles con <a href=\"https://www.texacocentralamerica.com/honduras\" target=\"_blank\" rel=\"noopener\">Texaco Inc.</a>, en la industria de partes industriales con <a href=\"https://www.centraldemanguerashn.com/\" target=\"_blank\" rel=\"noopener\">The Goodyear Tire &amp; Rubber Company</a>, y en el ámbito de la seguridad con <a href=\"https://www.g4s.com/en-hn\" target=\"_blank\" rel=\"noopener\">G4S Secure Solutions International</a>. Su pasión por el desarrollo humano e institucional lo ha llevado a consolidarse como un experto de alcance internacional, participando en proyectos significativos en América Latina, Estados Unidos, Europa del Este y África.",
        "_links": {
            "self": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540",
                    "targetHints": {
                        "allow": [
                            "GET",
                            "POST",
                            "PUT",
                            "PATCH",
                            "DELETE"
                        ]
                    }
                }
            ],
            "collection": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
                }
            ],
            "about": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types/stm_staff"
                }
            ],
            "version-history": [
                {
                    "count": 58,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540/revisions"
                }
            ],
            "predecessor-version": [
                {
                    "id": 10206,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540/revisions/10206"
                }
            ],
            "wp:featuredmedia": [
                {
                    "embeddable": true,
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media/7534"
                }
            ],
            "wp:attachment": [
                {
                    "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media?parent=7540"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": "https://api.w.org/{rel}",
                    "templated": true
                }
            ]
        }
    }
]
```

GET <https://consultoria-aplicada.com/wp-json/wp/v2/stm_staff/{id}>

corrected endpoint according to confit.py.ENSPOINT_MAP:
GET <https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540>
Result:

```json
{
    "id": 7540,
    "date": "2024-11-23T01:23:01",
    "date_gmt": "2024-11-23T07:23:01",
    "guid": {
        "rendered": "https://consultoria-aplicada.com/staff/alfredo-enrique-umana/"
    },
    "modified": "2025-04-11T15:34:06",
    "modified_gmt": "2025-04-11T21:34:06",
    "slug": "alfredo-enrique-umana",
    "status": "publish",
    "type": "stm_staff",
    "link": "https://consultoria-aplicada.com/equipo/alfredo-enrique-umana/",
    "title": {
        "rendered": "Alfredo Enrique Umaña"
    },
    "content": {
        "rendered": "\t\t<div data-elementor-type=\"wp-post\" data-elementor-id=\"7540\" class=\"elementor elementor-7540 elementor-461\" data-elementor-post-type=\"stm_staff\">\n\t\t\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-aa6622c elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"aa6622c\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-aa6676e\" data-id=\"aa6676e\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-aa66bd4 elementor-widget elementor-widget-vc_custom_heading\" data-id=\"aa66bd4\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading capitalize consulting_heading_font  text_align_left has_subtitle\" ><h2 style=\"text-align: left;font-weight:700\" class=\"consulting-custom-title\">Alfredo Enrique Umaña<span class=\"subtitle\">Fundador y Consultor Principal</span></h2></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-e63b71f e-flex e-con-boxed e-con e-parent\" data-id=\"e63b71f\" data-element_type=\"container\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t<div class=\"e-con-inner\">\n\t\t<div class=\"elementor-element elementor-element-249fc9a e-con-full e-flex e-con e-child\" data-id=\"249fc9a\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-82caa28 img-box-shadow elementor-widget elementor-widget-image\" data-id=\"82caa28\" data-element_type=\"widget\" data-widget_type=\"image.default\">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<img fetchpriority=\"high\" decoding=\"async\" width=\"1024\" height=\"1024\" src=\"https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1024x1024.jpeg\" class=\"attachment-large size-large wp-image-7534\" alt=\"Alfredo Enrique Umaña Martínez\" srcset=\"https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1024x1024.jpeg 1024w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-300x300.jpeg 300w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-150x150.jpeg 150w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-768x768.jpeg 768w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-1536x1536.jpeg 1536w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-2048x2048.jpeg 2048w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-50x50.jpeg 50w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-320x320.jpeg 320w, https://consultoria-aplicada.com/wp-content/uploads/2024/11/Alfredo-Umana-large-900x900.jpeg 900w\" sizes=\"(max-width: 1024px) 100vw, 1024px\" />\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-35395d2 e-con-full e-flex e-con e-child\" data-id=\"35395d2\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-5dd9c5d elementor-widget elementor-widget-vc_custom_heading\" data-id=\"5dd9c5d\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><div style=\"font-size: 16px;color: #222222;text-align: left;line-height: 22px;font-weight:700\" class=\"consulting-custom-title\">áreas de experiencia\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-8ce9f5c elementor-widget elementor-widget-text-editor\" data-id=\"8ce9f5c\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<ul style=\"font-size: 13px; line-height: 18px;\">\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Desarrollo Organizacional</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Manejo del Cambio</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Compression Planning</span></li>\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Estrategias de Crecimiento</span></li>\n</ul>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t<div class=\"elementor-element elementor-element-59abb71 e-con-full e-flex e-con e-child\" data-id=\"59abb71\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-2de6f3f elementor-widget elementor-widget-vc_custom_heading\" data-id=\"2de6f3f\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><div style=\"font-size: 16px;color: #222222;text-align: left;line-height: 22px;font-weight:700\" class=\"consulting-custom-title\">educación\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-8e2927f elementor-widget elementor-widget-text-editor\" data-id=\"8e2927f\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<ul style=\"font-size: 13px; line-height: 18px;\">\n<li><span style=\"color: #002e5b; text-shadow: #002e5b 0px 0px 0px !important;\">Máster en Administración de Empresas, Instituto Centroamericano de Administración de Empresas — INCAE</span></li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\"><span style=\"color: #002e5b;\">Licenciado en Administración de Empresas, Universidad Nacional Autónoma de Honduras</span></li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\">MBA, Rotterdam School of Management, Erasmus University</li>\n<li style=\"text-shadow: #777777 0px 0px 0px !important;\"> </li>\n</ul>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68855 easy-read elementor-widget elementor-widget-text-editor\" data-id=\"aa68855\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>La distintiva metodología de Alfredo Enrique Umaña en el fortalecimiento organizacional se ha consolidado como referente regional tras veinte años de trayectoria, integrando innovación estratégica con rigurosa medición de resultados. Su excepcional capacidad para potenciar equipos directivos y optimizar estructuras operacionales lo posiciona como asesor estratégico de confianza para corporaciones e instituciones sin fines de lucro. Su propuesta de valor se distingue por catalizar transformaciones organizacionales profundas y sostenibles, generando impacto tangible y cuantificable en los indicadores clave de desempeño de sus clientes.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68a77 elementor-widget elementor-widget-text-editor\" data-id=\"aa68a77\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<blockquote>\n<p>Consultoría Aplicada pone a disposición de sus clientes los talentos, habilidades y experiencia profesional de nuestros consultores, quienes brindan un enorme aporte al logro de las metas transformadoras de los procesos de los servicios que ofrecemos.</p>\n</blockquote>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-aa68c97 elementor-widget elementor-widget-text-editor\" data-id=\"aa68c97\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>Antes de fundar Consultoría Aplicaa, Alfredo manejó posiciones de dirección en importantes empresas locales y transnacionales, en las que brindó enormes aportes en el desarrollo de su desempeño.</p>\n<p>Como ávido consumidor de conocimiento y creador de contenido relevante para el crecimiento y mejora empresarial, Alfredo también comparte periódicamente sus acertados consejos en múltiples publicaciones en nuestro blog, carta de noticias y redes sociales.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-c736f70 elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"c736f70\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-8a8a120\" data-id=\"8a8a120\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-43fb74c elementor-widget elementor-widget-vc_custom_heading\" data-id=\"43fb74c\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading no_stripe consulting_heading_font  text_align_left\" ><h4 style=\"color: #222222;text-align: left;font-weight:700\" class=\"consulting-custom-title\">publicaciones\n</h4></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-0720fcc img-box-shadow elementor-widget elementor-widget-stm_news\" data-id=\"0720fcc\" data-element_type=\"widget\" data-widget_type=\"stm_news.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\t\t\t\t<div class=\"consulting_posts_box consulting_elementor_posts\n\t\t\t\tgrid\t\t\t\t\">\n\t\t\t\t\t<ul class=\"consulting_posts posts_per_row_2\">\n\t\t\t\t\t\t<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2025/03/Renovacion-Empresarial-350x250.jpg' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\">Renovación empresarial: Cómo evitar el deterioro silencioso</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/gestion-del-cambio/\" class=\"category category-1\">Gestión del Cambio</a>, <a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-2\">Lecciones Empresariales</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Al igual que una casa, una empresa necesita mantenimiento constante para no perder su propósito ni pertinencia. Descubre cómo renovar tu negocio para que vuelva a brillar.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">marzo 18, 2025</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/renovacion-empresarial-como-evitar-el-deterioro-silencioso/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2024/12/ahora-lo-vimos-350x250.png' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\">Cómo convertir un año difícil en la base para un éxito futuro</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/estrategias-de-reaccion-rapida/\" class=\"category category-1\">Estrategias de Reacción Rápida</a>, <a href=\"https://consultoria-aplicada.com/categoria/gestion-del-cambio/\" class=\"category category-2\">Gestión del Cambio</a><a href=\"https://consultoria-aplicada.com/categoria/innovacion-en-crisis/\" class=\"category category-3\">Innovación en Crisis</a><a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-4\">Lecciones Empresariales</a><a href=\"https://consultoria-aplicada.com/categoria/lidesazgo-estrategico/\" class=\"category category-5\">Lidesazgo Estratégico</a><a href=\"https://consultoria-aplicada.com/categoria/productividad-y-planificacion/\" class=\"category category-6\">Productividad y Planificación</a><a href=\"https://consultoria-aplicada.com/categoria/resiliencia-organizacional/\" class=\"category category-7\">Resiliencia Organizacional</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Cuando enfrentamos desafíos inesperados, también encontramos lecciones valiosas. Aprende cómo convertir las dificultades en estrategias efectivas para avanzar con claridad, creatividad y compromiso.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">diciembre 4, 2024</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/como-convertir-un-periodo-dificil-en-la-base-para-un-exito-futuro/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n<li class=\"post_item\">\n\t<div class=\"post_inner\">\n\t\t\t\t\t<div class=\"image\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\">\n\t\t\t\t\t<img src='https://consultoria-aplicada.com/wp-content/uploads/2025/02/Sorprende-a-tus-clientes-350x250.jpg' alt='' />\t\t\t\t</a>\n\t\t\t</div>\n\t\t\t\t\t<div class=\"news_item_info content_left\">\n\t\t\t<h5 class=\"news_item_title line_under_title\">\n\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\">¡Sorprende a tus clientes y ellos te sorprenderán a ti!</a>\n\t\t\t</h5>\n\t\t\t\t\t\t\t<div class=\"category\">\n\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/categoria/cultura-organizacional/\" class=\"category category-0\">Cultura Organizacional</a>, <a href=\"https://consultoria-aplicada.com/categoria/innovacion/\" class=\"category category-1\">Innovación</a>, <a href=\"https://consultoria-aplicada.com/categoria/lecciones-empresariales/\" class=\"category category-2\">Lecciones Empresariales</a><a href=\"https://consultoria-aplicada.com/categoria/productividad-y-planificacion/\" class=\"category category-3\">Productividad y Planificación</a>\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class=\"news_info\">\n\t\t\t\t\t<p>Tres paradigmas transformadores para el servicio al cliente: abundancia vs. escasez, sastre vs. tienda, y destino vs. taxímetro. Descubra cómo superar expectativas desde una mentalidad de servicio genuino genera lealtad duradera y convierte relaciones comerciales en alianzas estratégicas.</p>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class=\"news_info_bottom\">\n\t\t\t\t\t\t\t\t\t<div class=\"date icon_before\">\n\t\t\t\t\t\t<span class=\"news_item_date\">noviembre 29, 2024</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<a href=\"https://consultoria-aplicada.com/sorprende-a-tus-clientes-y-ellos-te-sorprenderan-a-ti/\" class=\"news_item_button\">\n\t\t\t\t\t\tRead More<svg aria-hidden=\"true\" class=\"button_icon after_icon e-font-icon-svg e-fas-arrow-right\" viewBox=\"0 0 448 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z\"></path></svg>\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</div>\n\t\t</div>\n\t</div>\n</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-10daa0a elementor-widget elementor-widget-stm_staff_bottom\" data-id=\"10daa0a\" data-element_type=\"widget\" data-widget_type=\"stm_staff_bottom.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\"staff_bottom_wr consulting_elementor_staff_bottom\">\n    <div class=\"staff_bottom\">\n\t<h4 class=\"no_stripe\">detalles de contacto</h4>\n\t<div class=\"infos\">\n\t\t<div class=\"info\">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t<div class=\"info\">\n\t\t\t<div class=\"socials\">\n\t\t\t\t<p>Perfiles Sociales</p>\n\t\t\t\t<ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<section class=\"elementor-section elementor-top-section elementor-element elementor-element-b570414 elementor-section-boxed elementor-section-height-default elementor-section-height-default\" data-id=\"b570414\" data-element_type=\"section\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t\t<div class=\"elementor-container elementor-column-gap-default\">\n\t\t\t\t\t<div class=\"elementor-column elementor-col-25 elementor-top-column elementor-element elementor-element-918aa26\" data-id=\"918aa26\" data-element_type=\"column\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-e0ecff8 elementor-widget elementor-widget-vc_custom_heading\" data-id=\"e0ecff8\" data-element_type=\"widget\" data-widget_type=\"vc_custom_heading.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t<div class=\" vc_custom_heading  consulting_heading_font  text_align_left\" ><h4 style=\"text-align: left;font-weight:700\" class=\"consulting-custom-title\">contacto\n</h4></div>\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"elementor-element elementor-element-90783fc elementor-widget elementor-widget-text-editor\" data-id=\"90783fc\" data-element_type=\"widget\" data-widget_type=\"text-editor.default\">\n\t\t\t\t\t\t\t\t\t<p>Si tienes una consulta, no dudes en contactarnos.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t<div class=\"elementor-column elementor-col-75 elementor-top-column elementor-element elementor-element-3a45629\" data-id=\"3a45629\" data-element_type=\"column\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t<div class=\"elementor-widget-wrap elementor-element-populated\">\n\t\t\t\t\t\t<div class=\"elementor-element elementor-element-5db975e elementor-widget elementor-widget-stm_contact_form_7\" data-id=\"5db975e\" data-element_type=\"widget\" data-widget_type=\"stm_contact_form_7.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\n<div class=\"wpcf7 no-js\" id=\"wpcf7-f8238-o1\" lang=\"es-ES\" dir=\"ltr\" data-wpcf7-id=\"8238\">\n<div class=\"screen-reader-response\"><p role=\"status\" aria-live=\"polite\" aria-atomic=\"true\"></p> <ul></ul></div>\n<form action=\"/wp-json/wp/v2/equipo/7540#wpcf7-f8238-o1\" method=\"post\" class=\"wpcf7-form init\" aria-label=\"Formulario de contacto\" novalidate=\"novalidate\" data-status=\"init\">\n<div style=\"display: none;\">\n<input type=\"hidden\" name=\"_wpcf7\" value=\"8238\" />\n<input type=\"hidden\" name=\"_wpcf7_version\" value=\"6.0.6\" />\n<input type=\"hidden\" name=\"_wpcf7_locale\" value=\"es_ES\" />\n<input type=\"hidden\" name=\"_wpcf7_unit_tag\" value=\"wpcf7-f8238-o1\" />\n<input type=\"hidden\" name=\"_wpcf7_container_post\" value=\"0\" />\n<input type=\"hidden\" name=\"_wpcf7_posted_data_hash\" value=\"\" />\n<input type=\"hidden\" name=\"_wpcf7_recaptcha_response\" value=\"\" />\n</div>\n<div class=\"member_feedback\">\n    <div class=\"row\">\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"nombres\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Nombres\" value=\"\" type=\"text\" name=\"nombres\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"apellidos\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Apellidos\" value=\"\" type=\"text\" name=\"apellidos\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"email\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-email wpcf7-validates-as-required wpcf7-text wpcf7-validates-as-email\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Correo Electrónico\" value=\"\" type=\"email\" name=\"email\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"tel\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-tel wpcf7-text wpcf7-validates-as-tel\" aria-invalid=\"false\" placeholder=\"Teléfono\" value=\"\" type=\"tel\" name=\"tel\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"ciudad\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text wpcf7-validates-as-required\" aria-required=\"true\" aria-invalid=\"false\" placeholder=\"Ciudad\" value=\"\" type=\"text\" name=\"ciudad\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"estado\"><input size=\"40\" maxlength=\"400\" class=\"wpcf7-form-control wpcf7-text\" aria-invalid=\"false\" placeholder=\"Estado, Departamento o Provincia\" value=\"\" type=\"text\" name=\"estado\" /></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n                <span class=\"wpcf7-form-control-wrap\" data-name=\"pais\"><select class=\"wpcf7-form-control wpcf7-select\" aria-invalid=\"false\" name=\"pais\"><option value=\"\">Honduras</option><option value=\"Argentina\">Argentina</option><option value=\"Belice\">Belice</option><option value=\"Bolivia\">Bolivia</option><option value=\"Canadá\">Canadá</option><option value=\"Chile\">Chile</option><option value=\"Colombia\">Colombia</option><option value=\"Costa Rica\">Costa Rica</option><option value=\"Cuba\">Cuba</option><option value=\"Dominicana\">Dominicana</option><option value=\"Ecuador\">Ecuador</option><option value=\"El Salvador\">El Salvador</option><option value=\"Estados Unidos de América\">Estados Unidos de América</option><option value=\"Guatemala\">Guatemala</option><option value=\"México\">México</option><option value=\"Nicaragua\">Nicaragua</option><option value=\"Panamá\">Panamá</option><option value=\"Paraguay\">Paraguay</option><option value=\"Perú\">Perú</option><option value=\"Puerto Rico\">Puerto Rico</option><option value=\"Uruguay\">Uruguay</option><option value=\"Venezuela\">Venezuela</option><option value=\"Otro\">Otro</option></select></span>\n            </div>\n        </div>\n        <div class=\"col-lg-6 col-md-6 col-sm-6 col-xs-12\">\n            <div class=\"input-group\">\n               <button type=\"submit\" class=\"button size-lg icon_right\">ENVIAR<i class=\"fa fa-chevron-right\"></i></button>\n            </div>\n        </div>\n    </div>\n</div><p style=\"display: none !important;\" class=\"akismet-fields-container\" data-prefix=\"_wpcf7_ak_\"><label>&#916;<textarea name=\"_wpcf7_ak_hp_textarea\" cols=\"45\" rows=\"8\" maxlength=\"100\"></textarea></label><input type=\"hidden\" id=\"ak_js_1\" name=\"_wpcf7_ak_js\" value=\"250\"/><script>document.getElementById( \"ak_js_1\" ).setAttribute( \"value\", ( new Date() ).getTime() );</script></p><div class=\"wpcf7-response-output\" aria-hidden=\"true\"></div>\n</form>\n</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t\t\t\t</div>\n\t\t</div>\n\t\t\t\t\t</div>\n\t\t</section>\n\t\t<div class=\"elementor-element elementor-element-d63bf4f third_bg_color e-flex e-con-boxed e-con e-parent\" data-id=\"d63bf4f\" data-element_type=\"container\" data-settings=\"{&quot;background_background&quot;:&quot;classic&quot;}\">\n\t\t\t\t\t<div class=\"e-con-inner\">\n\t\t<div class=\"elementor-element elementor-element-75d4c2f e-con-full e-flex e-con e-child\" data-id=\"75d4c2f\" data-element_type=\"container\">\n\t\t\t\t<div class=\"elementor-element elementor-element-0f41895 elementor-widget elementor-widget-vc_cta\" data-id=\"0f41895\" data-element_type=\"widget\" data-widget_type=\"vc_cta.default\">\n\t\t\t\t<div class=\"elementor-widget-container\">\n\t\t\t\t\t\n<div class=\"ce_cta ce_cta_f6c2cc24f9f259f1bb160a808fcc31f7 ce_text_left third_bg_color add_button_right btn_align_right btn_button_block_true btn_has_icon btn_has_icon_on_the_right\" id=\"\">\n\t<div class=\"ce_cta__content\">\n\t\t<div class=\"ce_cta__content__header\">\n\t\t\t<h2  class='ce_cta__content__title '>¿Necesitas una consultoría de primer nivel para tu empresa?</h2>\t\t</div>\n\t\t\t</div>\n\n\t\t<div class=\"ce_cta__action\">\n\t\t<a\n\t\t\thref=\"#\"\n\t\t\t\t\t\ttarget=\"_self\"\n\t\t\tclass=\"button\n\t\t\t\t\t\">\n\t\t\t<span>solicitar propuesta</span>\n\t\t\t\t\t\t<i class=\"fa fa-chevron-right\"></i>\n\t\t\t\t\t</a>\n\t</div>\n\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t",
        "protected": false
    },
    "excerpt": {
        "rendered": "<p>La distintiva metodología de Alfredo Enrique Umaña en el fortalecimiento organizacional se ha consolidado como referente regional tras veinte años de trayectoria, integrando innovación estratégica con rigurosa medición de resultados. Su excepcional capacidad para potenciar equipos directivos y optimizar estructuras operacionales lo posiciona como asesor estratégico de confianza para corporaciones e instituciones sin fines de lucro. Su propuesta de valor se distingue por catalizar transformaciones organizacionales profundas y sostenibles, generando impacto tangible y cuantificable en los indicadores clave de desempeño de sus clientes.</p>\n",
        "protected": false
    },
    "featured_media": 7534,
    "template": "",
    "class_list": [
        "post-7540",
        "stm_staff",
        "type-stm_staff",
        "status-publish",
        "has-post-thumbnail",
        "hentry"
    ],
    "acf": [],
    "acf_experiencia": "<ul>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/planificacion-estrategica/\">Planificación Estratégica</a></li>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/formacion-corporativa/\">Formación Corporativa</a></li>\r\n \t<li><a href=\"https://consultoria-aplicada.com/servicio/coaching-ejecutivo-avanzado/\">Coaching Ejecutivo</a></li>\r\n</ul>",
    "acf_educacion": "<ul>\r\n \t<li>Maestría en Administración de Empresas (MBA) — INCAE, Alajuela, Costa Rica</li>\r\n \t<li>Especialización en Liderazgo e Inteligencia Emocional — Trinity University, Chicago, IL, USA</li>\r\n \t<li>Certificación en Planificación Visual — Compression Planning Institute, Pittsburgh, PA, USA</li>\r\n</ul>",
    "acf_extra": "Alfredo inició su trayectoria profesional como consultor en <a href=\"https://www2.deloitte.com/hn/es.html\" target=\"_blank\" rel=\"noopener\">Deloitte &amp; Touche Business Solutions S.A.</a>, después de haber ocupado roles gerenciales en diversas industrias. Entre estas, destacan su experiencia en el sector de combustibles con <a href=\"https://www.texacocentralamerica.com/honduras\" target=\"_blank\" rel=\"noopener\">Texaco Inc.</a>, en la industria de partes industriales con <a href=\"https://www.centraldemanguerashn.com/\" target=\"_blank\" rel=\"noopener\">The Goodyear Tire &amp; Rubber Company</a>, y en el ámbito de la seguridad con <a href=\"https://www.g4s.com/en-hn\" target=\"_blank\" rel=\"noopener\">G4S Secure Solutions International</a>. Su pasión por el desarrollo humano e institucional lo ha llevado a consolidarse como un experto de alcance internacional, participando en proyectos significativos en América Latina, Estados Unidos, Europa del Este y África.",
    "_links": {
        "self": [
            {
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540",
                "targetHints": {
                    "allow": [
                        "GET",
                        "POST",
                        "PUT",
                        "PATCH",
                        "DELETE"
                    ]
                }
            }
        ],
        "collection": [
            {
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo"
            }
        ],
        "about": [
            {
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/types/stm_staff"
            }
        ],
        "version-history": [
            {
                "count": 58,
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540/revisions"
            }
        ],
        "predecessor-version": [
            {
                "id": 10206,
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/equipo/7540/revisions/10206"
            }
        ],
        "wp:featuredmedia": [
            {
                "embeddable": true,
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media/7534"
            }
        ],
        "wp:attachment": [
            {
                "href": "https://consultoria-aplicada.com/wp-json/wp/v2/media?parent=7540"
            }
        ],
        "curies": [
            {
                "name": "wp",
                "href": "https://api.w.org/{rel}",
                "templated": true
            }
        ]
    }
}
```
