const API_URL = import.meta.env.VITE_API_URL;

export function getAuthHeaders(): HeadersInit {
  const token = localStorage.getItem('access_token');
  return {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` }),
  };
}

export async function apiRequest<T>(
  endpoint: string,
  options: RequestInit & {
    useFormData?: boolean;
    formData?: URLSearchParams;
  } = {}
): Promise<T> {
  const { useFormData, formData, ...fetchOptions } = options;
  const url = `${API_URL}${endpoint}`;

  // Get headers - override Content-Type for form data
  const headers = useFormData
    ? { 'Content-Type': 'application/x-www-form-urlencoded' }
    : getAuthHeaders();

  const response = await fetch(url, {
    ...fetchOptions,
    headers: {
      ...headers,
      ...fetchOptions.headers,
    },
    body: useFormData ? formData : fetchOptions.body,
  });

  if (!response.ok) {
    const error = await response
      .json()
      .catch(() => ({ detail: 'Request failed' }));
    throw new Error(error.detail || `HTTP error! status: ${response.status}`);
  }

  return response.json();
}
