import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const migratedBaseSchema = z.object({
  title: z.string(),
  slug: z.string(),
  date: z.coerce.date(),
  excerpt: z.string().default(''),
  seo_title: z.string().optional(),
  seo_description: z.string().optional(),
  featured_image: z.string().optional(),
  featured_image_id: z.number().optional(),
  og_image: z.string().optional(),
  canonical: z.string().optional(),
  link: z.string().optional(),
  status: z.string().optional(),
  type: z.string().optional(),
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: migratedBaseSchema,
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: migratedBaseSchema.extend({
    categories: z.array(z.string()).default([]),
  }),
});

export const collections = { pages, posts };
