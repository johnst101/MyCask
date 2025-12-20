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
  const baseHeaders = useFormData
    ? { 'Content-Type': 'application/x-www-form-urlencoded' }
    : getAuthHeaders();

  // Merge headers properly - convert to plain object for easier merging
  const headersObj: Record<string, string> = {
    ...(baseHeaders as Record<string, string>),
    ...(fetchOptions.headers &&
    typeof fetchOptions.headers === 'object' &&
    !(fetchOptions.headers instanceof Headers)
      ? (fetchOptions.headers as Record<string, string>)
      : {}),
  };

  const response = await fetch(url, {
    ...fetchOptions,
    headers: headersObj,
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
