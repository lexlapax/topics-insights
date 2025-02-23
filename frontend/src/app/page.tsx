'use client';

import { Box, Container, Heading, Text, VStack } from '@chakra-ui/react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const { data: healthCheck, isLoading, error } = useQuery({
    queryKey: ['health'],
    queryFn: async () => {
      const response = await axios.get(`${API_URL}/api/v1/health`);
      return response.data;
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
          {isLoading && <Text>Checking system status...</Text>}
          {error && <Text color="red.500">Error connecting to backend</Text>}
          {healthCheck && (
            <VStack align="stretch" spacing={2}>
              <Text>API Status: {healthCheck.services.api}</Text>
              <Text>Database Status: {healthCheck.services.database}</Text>
              <Text>LLM Status: {healthCheck.services.llm}</Text>
            </VStack>
          )}
        </Box>
      </VStack>
    </Container>
  );
} 