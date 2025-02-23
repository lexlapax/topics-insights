'use client';

import { Box, Container, Heading, Text, VStack } from '@chakra-ui/react';
import { useQuery } from '@tanstack/react-query';

interface HealthCheckResponse {
  status: string;
  version: string;
}

export default function Home() {
  const { data: healthCheck, isLoading, error } = useQuery<HealthCheckResponse>({
    queryKey: ['healthCheck'],
    queryFn: async () => {
      const response = await fetch('http://localhost:8000/');
      return response.json();
    },
  });

  return (
    <Container maxW="container.xl" py={10}>
      <VStack spacing={6} align="stretch">
        <Heading as="h1" size="2xl">
          Topic Insights
        </Heading>
        <Text fontSize="xl">
          Your AI-powered platform for topic-based content aggregation and analysis
        </Text>

        <Box bg="gray.50" p={6} borderRadius="md">
          <Heading as="h2" size="md" mb={4}>
            System Status
          </Heading>
          {isLoading && <Text>Loading status...</Text>}
          {error && <Text color="red.500">Error loading status</Text>}
          {healthCheck && (
            <Text>Status: {healthCheck.status}</Text>
          )}
        </Box>
      </VStack>
    </Container>
  );
} 