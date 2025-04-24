<?php
/**
 * SEO Metadata Generator - WordPress REST API Integration
 * 
 * This file contains WordPress functions to expose Rank Math SEO fields through the WordPress REST API.
 * It enables the SEO Metadata Generator tool to read and update SEO metadata programmatically.
 * Add the contents of this file to your WordPress child theme's functions.php file.
 * 
 * @package SEO_Metadata_Generator
 * @version 1.0.0
 * @author Adalberto H. Vega
 * @license MIT
 */

/**
 * Exposes Rank Math SEO fields in the WordPress REST API for all public post types.
 * 
 * This function registers custom REST API fields for Rank Math SEO metadata,
 * allowing external applications to read and update SEO data through the API.
 * 
 * @since 1.0.0
 * @hook rest_api_init
 * @return void
 */
function expose_rankmath_fields() {
    // Register fields for all post types
    $post_types = get_post_types(array('public' => true));
    
    foreach ($post_types as $post_type) {
        register_rest_field(
            $post_type,
            'rank_math',
            array(
                'get_callback' => 'get_rankmath_fields',
                'update_callback' => 'update_rankmath_fields',
                'schema' => array(
                    'description' => 'Rank Math SEO fields',
                    'type' => 'object',
                    'properties' => array(
                        'title' => array(
                            'type' => 'string',
                            'description' => 'SEO Title'
                        ),
                        'description' => array(
                            'type' => 'string',
                            'description' => 'Meta Description'
                        ),
                        'focus_keyword' => array(
                            'type' => 'string',
                            'description' => 'Focus Keyword'
                        ),
                        'canonical_url' => array(
                            'type' => 'string',
                            'description' => 'Canonical URL'
                        ),
                        'og_title' => array(
                            'type' => 'string',
                            'description' => 'Open Graph Title'
                        ),
                        'og_description' => array(
                            'type' => 'string',
                            'description' => 'Open Graph Description'
                        ),
                        'twitter_title' => array(
                            'type' => 'string',
                            'description' => 'Twitter Card Title'
                        ),
                        'twitter_description' => array(
                            'type' => 'string',
                            'description' => 'Twitter Card Description'
                        )
                    )
                )
            )
        );
    }
}
add_action('rest_api_init', 'expose_rankmath_fields');

/**
 * Retrieves Rank Math SEO fields for a given post.
 * 
 * @since 1.0.0
 * @param array $object The post object
 * @param string $field_name The field name
 * @param WP_REST_Request $request The REST request
 * @return array Array of Rank Math SEO fields
 */
function get_rankmath_fields($object, $field_name, $request) {
    $post_id = $object['id'];
    
    return array(
        'title' => get_post_meta($post_id, 'rank_math_title', true),
        'description' => get_post_meta($post_id, 'rank_math_description', true),
        'focus_keyword' => get_post_meta($post_id, 'rank_math_focus_keyword', true),
        'canonical_url' => get_post_meta($post_id, 'rank_math_canonical_url', true),
        'og_title' => get_post_meta($post_id, 'rank_math_og_title', true),
        'og_description' => get_post_meta($post_id, 'rank_math_og_description', true),
        'twitter_title' => get_post_meta($post_id, 'rank_math_twitter_title', true),
        'twitter_description' => get_post_meta($post_id, 'rank_math_twitter_description', true)
    );
}

/**
 * Updates Rank Math SEO fields for a given post.
 * 
 * @since 1.0.0
 * @param array $value The new field values
 * @param WP_Post $object The post object
 * @param string $field_name The field name
 * @return bool True on success
 */
function update_rankmath_fields($value, $object, $field_name) {
    $post_id = $object->ID;
    
    if (isset($value['title'])) {
        update_post_meta($post_id, 'rank_math_title', sanitize_text_field($value['title']));
    }
    if (isset($value['description'])) {
        update_post_meta($post_id, 'rank_math_description', sanitize_textarea_field($value['description']));
    }
    if (isset($value['focus_keyword'])) {
        update_post_meta($post_id, 'rank_math_focus_keyword', sanitize_text_field($value['focus_keyword']));
    }
    if (isset($value['canonical_url'])) {
        update_post_meta($post_id, 'rank_math_canonical_url', esc_url_raw($value['canonical_url']));
    }
    if (isset($value['og_title'])) {
        update_post_meta($post_id, 'rank_math_og_title', sanitize_text_field($value['og_title']));
    }
    if (isset($value['og_description'])) {
        update_post_meta($post_id, 'rank_math_og_description', sanitize_textarea_field($value['og_description']));
    }
    if (isset($value['twitter_title'])) {
        update_post_meta($post_id, 'rank_math_twitter_title', sanitize_text_field($value['twitter_title']));
    }
    if (isset($value['twitter_description'])) {
        update_post_meta($post_id, 'rank_math_twitter_description', sanitize_textarea_field($value['twitter_description']));
    }
    
    return true;
}

/**
 * Exposes Rank Math SEO fields for taxonomies in the WordPress REST API.
 * 
 * This function registers custom REST API fields for Rank Math SEO metadata
 * for taxonomies, allowing external applications to read and update SEO data
 * for categories, tags, and other taxonomies.
 * 
 * @since 1.0.0
 * @hook rest_api_init
 * @return void
 */
function expose_rankmath_taxonomy_fields() {
    $taxonomies = get_taxonomies(array('public' => true));
    
    foreach ($taxonomies as $taxonomy) {
        register_rest_field(
            $taxonomy,
            'rank_math',
            array(
                'get_callback' => 'get_rankmath_taxonomy_fields',
                'update_callback' => 'update_rankmath_taxonomy_fields',
                'schema' => array(
                    'description' => 'Rank Math SEO fields for taxonomies',
                    'type' => 'object',
                    'properties' => array(
                        'title' => array(
                            'type' => 'string',
                            'description' => 'SEO Title'
                        ),
                        'description' => array(
                            'type' => 'string',
                            'description' => 'Meta Description'
                        ),
                        'focus_keyword' => array(
                            'type' => 'string',
                            'description' => 'Focus Keyword'
                        )
                    )
                )
            )
        );
    }
}
add_action('rest_api_init', 'expose_rankmath_taxonomy_fields');

/**
 * Retrieves Rank Math SEO fields for a given taxonomy term.
 * 
 * @since 1.0.0
 * @param array $object The term object
 * @param string $field_name The field name
 * @param WP_REST_Request $request The REST request
 * @return array Array of Rank Math SEO fields
 */
function get_rankmath_taxonomy_fields($object, $field_name, $request) {
    $term_id = $object['id'];
    
    return array(
        'title' => get_term_meta($term_id, 'rank_math_title', true),
        'description' => get_term_meta($term_id, 'rank_math_description', true),
        'focus_keyword' => get_term_meta($term_id, 'rank_math_focus_keyword', true)
    );
}

/**
 * Updates Rank Math SEO fields for a given taxonomy term.
 * 
 * @since 1.0.0
 * @param array $value The new field values
 * @param WP_Term $object The term object
 * @param string $field_name The field name
 * @return bool True on success
 */
function update_rankmath_taxonomy_fields($value, $object, $field_name) {
    $term_id = $object->term_id;
    
    if (isset($value['title'])) {
        update_term_meta($term_id, 'rank_math_title', sanitize_text_field($value['title']));
    }
    if (isset($value['description'])) {
        update_term_meta($term_id, 'rank_math_description', sanitize_textarea_field($value['description']));
    }
    if (isset($value['focus_keyword'])) {
        update_term_meta($term_id, 'rank_math_focus_keyword', sanitize_text_field($value['focus_keyword']));
    }
    
    return true;
} 